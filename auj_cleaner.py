import shutil

class AUJCleaner():

    def __init__(self, data, is_dict:False):
        dirs = []
        
        if is_dict:
            dirs = list(data.values())
        else:
            dirs = data
        
        self.data=dirs

    def clean(self, verbose=False):
        for d in self.data:
            shutil.rmtree(d, ignore_errors=True)
            
            if verbose:
                print(f"Directory deleted: {d}")

