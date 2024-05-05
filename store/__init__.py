


def load(module,variable):
    from ui.ui_print import ui_print
    from ui.ui_print import ui_settings
    from ui.ui_print import config_dir
    from base import pickle
    from base import os
    import json
    cache = []
    try:
        filename = config_dir + '/' + module + "_" + variable + '.pkl'
        if os.path.exists(filename):
            ui_print("["+module+"] reading cached "+variable+" file ... " + filename)
            ##ui_print(json.dumps(cache))
            with open(filename, 'rb') as f:
                cache = pickle.load(f)
            ui_print("done")
    except Exception as e: 
        ui_print("["+module+"] error: couldnt read cached "+variable+" file. " + e)       
        cache = []
    return cache

def save(cache,module,variable):
    from ui.ui_print import ui_print
    from ui.ui_print import ui_settings
    from ui.ui_print import config_dir
    from base import pickle
    from base import os
    import json
    try:
        filename = config_dir + '/' + module + "_" + variable + '.pkl'
        ui_print("["+module+"] writing cached "+variable+" file ...")
        ##ui_print(json.dumps(cache))
        with open(filename, 'wb') as f:
            pickle.dump(cache, f)
        ui_print("done")
    except:
        ui_print("["+module+"] error: couldnt write cached "+variable+" file. " + e) 
