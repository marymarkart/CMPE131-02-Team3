from app import myapp_obj
<<<<<<< HEAD
from app import os

if __name__=="__main__":
    myapp_obj.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))
=======
>>>>>>> allen_branch

myapp_obj.run()
