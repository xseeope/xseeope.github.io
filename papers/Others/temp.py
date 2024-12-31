def save_annual_data(self):
        if (
            op.isfile(self.log_file_name)
            and op.isfile(self.labels_filename)
            and op.isfile(self.images_filename)
        ):
            print("Found pregenerated file {}".format(self.file_name))
            return
        print(f"Generating {self.file_name}")
        self.df = eqd.get_processed_US_data_by_year(self.year)
        self.stock_id_list = np.unique(self.df.index.get_level_values("StockID"))
        dtype_dict, feature_list = self._get_feature_and_dtype_list()
        data_miss = np.zeros(6)
        data_dict = {
            feature: np.empty(len(self.stock_id_list) * 60, dtype=dtype_dict[feature])
            for feature in feature_list
        }
        data_dict["image"] = np.empty(
            [len(self.stock_id_list) * 60, self.width * self.height],
            dtype=dtype_dict["image"],
        )
        data_dict["image"].fill(np.nan)

        sample_num = 0
        # import pdb;pdb.set_trace()
        iterator = (
            tqdm(self.stock_id_list)
            if (self.allow_tqdm and "tqdm" in sys.modules)
            else self.stock_id_list
        )
        for i, stock_id in enumerate(iterator):
            stock_df = self.df.xs(stock_id, level=1).copy()
            stock_df = stock_df.reset_index()
            dates = eqd.get_period_end_dates(self.freq)
            dates = dates[dates.year == self.year]
            # import pdb; pdb.set_trace()

            for j, date in enumerate(dates):
                try:
                    image_label_data = self._generate_daily_features(stock_df, date)

                    if type(image_label_data) is dict:
                        if (i < 2) and (j == 0):
                            image_label_data["image"].save(
                                op.join(
                                    self.image_save_dir,
                                    f"{self.file_name}_{stock_id}_{date.strftime('%Y%m%d')}.png",
                                )
                            )

                        image_label_data["StockID"] = stock_id
                        im_arr = np.frombuffer(
                            image_label_data["image"].tobytes(), dtype=np.uint8
                        )
                        assert im_arr.size == self.width * self.height
                        data_dict["image"][sample_num, :] = im_arr[:]
                        for feature in [x for x in feature_list if x != "image"]:
                            data_dict[feature][sample_num] = image_label_data[feature]
                        sample_num += 1
                    elif type(image_label_data) is int:
                        data_miss[image_label_data] += 1
                    else:
                        raise ValueError
                except ChartGenerationError:
                    print(f"DGP Error on {stock_id} {date}")
                    continue
        for feature in feature_list:
            data_dict[feature] = data_dict[feature][:sample_num]

        
        # import pdb; pdb.set_trace()
        fp_x = np.memmap(
            self.images_filename,
            dtype=np.uint8,
            mode="w+",
            shape=data_dict["image"].shape,
        )
        fp_x[:] = data_dict["image"][:]
        del fp_x
        print(f"Save image data to {self.images_filename}")
        data_dict = {x: data_dict[x] for x in data_dict.keys() if x != "image"}
        pd.DataFrame(data_dict).to_feather(self.labels_filename)
        print(f"Save label data to {self.labels_filename}")
        log_file = open(self.log_file_name, "w+")
        log_file.write(
            "total_dates:%d total_missing:%d type0:%d type1:%d type2:%d type3:%d type4:%d type5:%d"
            % (
                sample_num,
                sum(data_miss),
                data_miss[0],
                data_miss[1],
                data_miss[2],
                data_miss[3],
                data_miss[4],
                data_miss[5],
            )
        )
        log_file.close()
        print(f"Save log file to {self.log_file_name}")
