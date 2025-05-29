class LocalCVEReader:
    filepath = ""
    first_year = 1999
    current_year = 2025

    def access_folders(self, filepath: str):
        folderpath = ""
        for i in range(self.current_year - self.first_year):
            folderpath = filepath + "/" + str(self.first_year + i)
        return
    def batch_files(self, folder_path : str):

        return
    pass