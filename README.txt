
$$$$$$$\                            $$\       $$\      $$\                                                                                                                                                                                                                                                                       
$$  __$$\                           $$ |      $$$\    $$$ |                                                                                                                                                                                                                                                                      
$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$$ |      $$$$\  $$$$ | $$$$$$\                                                                                                                                                                                                                                                              
$$$$$$$  |$$  __$$\  \____$$\ $$  __$$ |      $$\$$\$$ $$ |$$  __$$\                                                                                                                                                                                                                                                             
$$  __$$< $$$$$$$$ | $$$$$$$ |$$ /  $$ |      $$ \$$$  $$ |$$$$$$$$ |                                                                                                                                                                                                                                                            
$$ |  $$ |$$   ____|$$  __$$ |$$ |  $$ |      $$ |\$  /$$ |$$   ____|                                                                                                                                                                                                                                                            
$$ |  $$ |\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |      $$ | \_/ $$ |\$$$$$$$\                                                                                                                                                                                                                                                             
\__|  \__| \_______| \_______| \_______|      \__|     \__| \_______|                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                 
$$$$$$$\                   $$$$$$\  $$\                 $$\             $$\     $$\                            $$$$$$\            $$\                                                      $$\       $$$$$$$$\           $$\ $$\              $$$$$$\            $$\       $$\                                                   
$$  __$$\                 $$  __$$\ $$ |                \__|            $$ |    \__|                          $$  __$$\           $$ |                                                     $$ |      $$  _____|          \__|$$ |            $$  __$$\           $$ |      $$ |                                                  
$$ |  $$ |$$\   $$\       $$ /  \__|$$$$$$$\   $$$$$$\  $$\  $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\        $$ /  \__| $$$$$$\  $$ |$$\    $$\  $$$$$$\         $$$$$$\  $$$$$$$\   $$$$$$$ |      $$ |       $$$$$$\  $$\ $$ |  $$\       $$ /  \__| $$$$$$$\ $$$$$$$\  $$ | $$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\  
$$$$$$$\ |$$ |  $$ |      $$ |      $$  __$$\ $$  __$$\ $$ |$$  _____|\_$$  _|  $$ | \____$$\ $$  __$$\       $$ |       \____$$\ $$ |\$$\  $$  |$$  __$$\        \____$$\ $$  __$$\ $$  __$$ |      $$$$$\    $$  __$$\ $$ |$$ | $$  |      \$$$$$$\  $$  _____|$$  __$$\ $$ |$$  __$$\ $$  _____|$$  _____|$$  __$$\ $$  __$$\ 
$$  __$$\ $$ |  $$ |      $$ |      $$ |  $$ |$$ |  \__|$$ |\$$$$$$\    $$ |    $$ | $$$$$$$ |$$ |  $$ |      $$ |       $$$$$$$ |$$ | \$$\$$  / $$ /  $$ |       $$$$$$$ |$$ |  $$ |$$ /  $$ |      $$  __|   $$ |  \__|$$ |$$$$$$  /        \____$$\ $$ /      $$ |  $$ |$$ |$$ /  $$ |\$$$$$$\  \$$$$$$\  $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |      $$ |  $$\ $$ |  $$ |$$ |      $$ | \____$$\   $$ |$$\ $$ |$$  __$$ |$$ |  $$ |      $$ |  $$\ $$  __$$ |$$ |  \$$$  /  $$ |  $$ |      $$  __$$ |$$ |  $$ |$$ |  $$ |      $$ |      $$ |      $$ |$$  _$$<        $$\   $$ |$$ |      $$ |  $$ |$$ |$$ |  $$ | \____$$\  \____$$\ $$   ____|$$ |      
$$$$$$$  |\$$$$$$$ |      \$$$$$$  |$$ |  $$ |$$ |      $$ |$$$$$$$  |  \$$$$  |$$ |\$$$$$$$ |$$ |  $$ |      \$$$$$$  |\$$$$$$$ |$$ |   \$  /   \$$$$$$  |      \$$$$$$$ |$$ |  $$ |\$$$$$$$ |      $$$$$$$$\ $$ |      $$ |$$ | \$$\       \$$$$$$  |\$$$$$$$\ $$ |  $$ |$$ |\$$$$$$  |$$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      
\_______/  \____$$ |       \______/ \__|  \__|\__|      \__|\_______/    \____/ \__| \_______|\__|  \__|       \______/  \_______|\__|    \_/     \______/        \_______|\__|  \__| \_______|      \________|\__|      \__|\__|  \__|       \______/  \_______|\__|  \__|\__| \______/ \_______/ \_______/  \_______|\__|      
          $$\   $$ |                                                                                                                                                                                                                                                                                                             
          \$$$$$$  |                                                                                                                                                                                                                                                                                                             
           \______/                                                                                                                                                                                                                                                                                                              

    Within this zip, you'll find a python file that you are able to run that stimulates, a system where a sound source is detected using a camera. There is a microphone array, and a microphone in each corner of the room
    if the sound source is closer to the said microphone it's intensity is higher than all of the other microphones. This is displayed within a graph after simulating. Down below is what you need to do to correctly run this
    simulation and what you should expect once doing so.


    1 - The files and applications needed
    You'll need an IDE that is able to compile python files, we used Visual Studio Code: https://code.visualstudio.com/.
    Then you'll need to install python, it must be a version higher than 3.10.
    After that, you'll have to open your command prompt in windows and type the following into it:
    pip install time
    pip install matplotlib.pyplot
    pip install numpy

    That should be everything needed to run our application.

    2 - Open the IDE, and run
    Open whatever IDE you downloaded to run the python file. There should be a play button in the top right. 
    This then begins the simulation, it will ask for a total of 6 inputs.

    The first is the room width
    The second one is the room height 
    ------------------------------------
    This will give you a NxN room

    The third input is the source's x position
    The fourth input is the source's y position
    ---------------------------------------------
    This initiates the source's (x,y)

    The fifth input is the feedback loops iterations
    The sixth one is the amount of seconds inbetween the iterations
    -----------------------------------------------------------------
    Begins the feedback loop for N amount of iterations

    Those are all the steps to be able to run our program. A graph should be expected at the end that shows you the position of the estimated source, the actual source, and where the camera would point to. 
    The 4 microphones intensities given the source position. In the terminal the actual position and the estimated will be shown to give you an idea of how accurate it is.


    
    
    
