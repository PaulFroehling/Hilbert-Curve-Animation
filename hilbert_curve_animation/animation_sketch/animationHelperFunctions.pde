/**
*Prepares the animation process for the 3D hilbert curve.
*PeasyCam is used to move the camera from the Starting Point to the Target point
*Start and Target are defined in globalVariables
*/
void setup3dAnimationCam(){
    cam = new PeasyCam(this, TS_START_DISTANCE); 
    cam.setRotations(TS_START_X, TS_START_Y, TS_START_Z);
    startState = cam.getState();
    PeasyCam tempCam = new PeasyCam(this, TS_TARGET_DISTANCE);
    tempCam.setRotations(TS_TARGET_X, TS_TARGET_Y, TS_TARGET_Z);
    endState = tempCam.getState();
    tempCam = null;
}


/**
 *Calculates the interpolated point for the current animation phase
 *
 * @return List of interpolated PVectors for the current step
 */
ArrayList<PVector> interpolateCurrentStep() {
  ArrayList<PVector> interpolatedPoints = new ArrayList<PVector>();
  ArrayList<PVector> startPoints = pointLists.get(animationPhase);
  ArrayList<PVector> targetPoints = pointLists.get(animationPhase + 1);

  for (int i = 0; i < startPoints.size(); i++) {
    PVector currentPoint = startPoints.get(i);
    PVector targetPoint = targetPoints.get(i);
    PVector newPoint = linInterpolation(currentPoint, targetPoint, N_STEPS, currentStep);
    interpolatedPoints.add(newPoint);
  }
  
  return interpolatedPoints;
}

/**
 * Resets the stepcounter and increases animationPhase by one
 * to transition to next phase of animation. 
 */
void proceedToNextAnimationPhase(){
    currentStep=0;       //If currentStep >= N_STEPS, interpolation from points in csv file n to csv file n+1 is done --> next animationPhase or done
    animationPhase ++;   //Increment animation Phase to interpolate between the current targetPoints and next csv File
}

/**
 * Checks if animation should be continued
 *
 * @return true, wenn die aktuelle Schrittzahl kleiner als N_STEPS ist und
 *         noch weitere Animationsphasen verfügbar sind; sonst false.
 */
boolean shouldAnimate(){
  return currentStep < N_STEPS && animationPhase < pointLists.size()-1;
}


/**
 * Performs linear interpolation between two PVectors based on the current step.
 *
 * @param currentPoint The starting point of the interpolation
 * @param targetPoint  The end point to interpolate toward
 * @param nSteps       Total number of interpolation steps
 * @param currentStep  Current step index (between 0 and nSteps)
 * @return A new PVector at the interpolated position
 */
PVector linInterpolation(PVector currentPoint, PVector targetPoint, int nSteps, int currentStep){

  PVector newPoint = new PVector();
  float dx = (targetPoint.x - currentPoint.x);
  float dy = (targetPoint.y - currentPoint.y);
  
  float stepSizeX = dx/nSteps * currentStep;
  float stepSizeY = dy/nSteps * currentStep;
  
  newPoint.x = currentPoint.x + stepSizeX;
  newPoint.y = currentPoint.y + stepSizeY;
  
  if(NUMBER_OF_DIMENSIONS==3){
    float dz = (targetPoint.z - currentPoint.z);
    float stepSizeZ = dz/nSteps * currentStep;
    newPoint.z = currentPoint.z + stepSizeZ;
  }
  
  return newPoint;
}


/**
 * Plots a set of 2D points on the canvas as colored ellipses.
 * The color is chosen based on the point's position in the overall list (by quadrant).
 *
 * @param currentPoints A list of PVectors to plot as points
 */
void plotPoints(ArrayList<PVector>currentPoints){
  
  for (int i = 0; i < currentPoints.size(); i++){
    PVector currentPoint = currentPoints.get(i);
    if(NUMBER_OF_DIMENSIONS == 2){
      int currentQuadrant = currentPoints.size()/4;
      fill(QUADRANT_COLORS[i/currentQuadrant]);
      stroke(QUADRANT_COLORS[i/currentQuadrant]);
      ellipse(currentPoint.x, currentPoint.y, 5, 5);
    }
     if (NUMBER_OF_DIMENSIONS == 3) {
      //Since my computer wasn't fast enough for those transformations, they are canceled here - only lines are drawn
      //pushMatrix();
      //translate(currentPoint.x, currentPoint.y, currentPoint.z);
      //sphere(2.5);
      //popMatrix();
    }
  }
}


/**
 * Draws lines between a sequence of 2D points.
 * Each line segment is colored based on its position in the list (by quadrant).
 *
 * @param currentPoints A list of PVectors to connect with lines
 */
void plotLines(ArrayList<PVector> currentPoints){
  for (int j = 0; j < currentPoints.size() - 1; j++) {
    int currentQuadrant = currentPoints.size()/4;
    stroke(QUADRANT_COLORS[j/currentQuadrant]);
   // strokeWeight(0.7);
    if(NUMBER_OF_DIMENSIONS == 2){
      line(currentPoints.get(j).x, currentPoints.get(j).y, currentPoints.get(j+1).x, currentPoints.get(j+1).y);
    }else if(NUMBER_OF_DIMENSIONS == 3){
      line(currentPoints.get(j).x, currentPoints.get(j).y, currentPoints.get(j).z, currentPoints.get(j+1).x, currentPoints.get(j+1).y, currentPoints.get(j+1).z);
    }
  }
}
