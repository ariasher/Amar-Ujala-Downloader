from shutil import rmtree


class AUJCleaner():
    '''
    Cleaner class to remove all the folders and images created by the downloader.
    '''

    def __init__(self, data, is_dict:False):
        '''
        Cleans all the temporary folders and files created.

        Requires:
            data[Dictonary/Tuple/List]: 
              The data is an object of dictionary, tuple or list type which includes the 
              directories which were created during the download of the newspaper.

              If data is a type of dictionary with KEY(string - dates) and VALUES(string - directories)
              then the values are extracted by itself but the flag should be set to True.
        
        Optional: 
            is_dict[Boolean]:
              The flag to indicate whether data is a type of dictionary or not. Default: False.
        '''
        
        dirs = []
        
        if is_dict:
            dirs = list(data.values())
        else:
            dirs = data
        
        self.__data=dirs

    def clean(self, verbose:bool = False) -> None:
        '''
        This method is used to clean/remove the directories which were created during the download period.

        Optional:
            verbose[Boolean]:
              This flag is used to show which directories have been created. Default: False.
        '''

        for d in self.__data:
            rmtree(d, ignore_errors=True)
            
            if verbose:
                print(f"Directory deleted: {d}")
