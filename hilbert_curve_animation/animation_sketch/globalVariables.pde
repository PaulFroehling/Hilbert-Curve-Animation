//GENERAL
int PLOT_WIDTH  = 800;
int PLOT_HEIGHT = 800;

// CSV DATA
String csv_path = "../../../skillings_intermediate_results/";                   //Set to your csv location. If you just copied the repo - this path should work
ArrayList<ArrayList<PVector>> pointLists = new ArrayList<ArrayList<PVector>>(); //List of csv file contents, loaded from csv_path


//ANIMATION/INTERPOLATION
int N_STEPS              = 140;         //Number of steps of the linear interpolation. Takes 120 steps to move from one point to the next
int HC_SCALING_FACTOR    = 12;          //The original points are concentrated to a very small area. Thus, some scaling is needed
int HC_BORDER_SIZE       = 10;          //When plotting the hilbert curve-leave HC_BORDER_SIZE pixels space to the border of the window
int NUMBER_OF_DIMENSIONS;               //Set automatically. Number of dimensions of the hilbert curve (2 or 3). 
int NUMBER_OF_BITS;                     //Set automatically. 

//ANIMATION 3D - TRACKING SHOT - COORDINATES AS QUATERNIONS
//cam.getRotations() can help to get the right positioning by drawing the object to the desired position by hand. 
float TS_START_X = -0.7335413;
float TS_START_Y = 0.5126788;
float TS_START_Z = 1.5498395;
float TS_START_DISTANCE = 1000;

float TS_TARGET_X = -0.7306068;
float TS_TARGET_Y = 0.65557873;
float TS_TARGET_Z = 0.8642945;
float TS_TARGET_DISTANCE = 2300;

CameraState startState;
CameraState endState;

int currentStep    = 0;      //Initially, the current step is 0. Increments during plotting
int animationPhase = 0;      //Phase: Animation/interpolation from csv n to csv n+1. Depending on how many csv files there are, there are more or less phases of interpolation.


//COLORS
color[] QUADRANT_COLORS = {   //Colors for lines and dots in the respective quadrants
    color(53, 175, 219),    
    color(107, 77, 240),    
    color(237, 77, 240),    
    color(245, 205, 61)   
  };

color BACKGROUND_COLOR = color(40);
