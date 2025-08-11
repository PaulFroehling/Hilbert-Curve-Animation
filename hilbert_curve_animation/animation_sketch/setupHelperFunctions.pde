/**
 * Imports a CSV file with two comma-separated float values per line
 * and returns them as a list of scaled and shifted PVectors.
 *
 * @param file A CSV file where each line contains two float values (x,y)
 * @return ArrayList of PVectors representing the scaled coordinates
*/
ArrayList<PVector> importCsvAsPVectorList(File file){
  ArrayList<PVector> points = new ArrayList<PVector>();
  String[] rows = loadStrings(file);
  
  for (int i = 0; i < rows.length; i++) {
    String row = rows[i];
    String[] parts = split(row, ',');
    PVector newPoint = new PVector();
    if (parts.length >= 2 && parts.length <=3) {                         //There should only be x and y coordinates if 2D ...
      newPoint.x = float(parts[0]) * HC_SCALING_FACTOR + HC_BORDER_SIZE; //The original distance between points is quite small and needs to be scaled for plotting
      newPoint.y = float(parts[1]) * HC_SCALING_FACTOR + HC_BORDER_SIZE;
    if (parts.length == 3) {                                             //...and x,y,z if 3D
      newPoint.z = float(parts[2]) * HC_SCALING_FACTOR + HC_BORDER_SIZE;
    }

    points.add(newPoint);
    }
  }
  return points;
}


/**
 * Loads all CSV files from a specified folder and converts their contents into point lists.
 * The resulting lists are added to the global `pointLists` array in reverse order.
 *
 * @param folder The folder containing CSV files to load
*/
void loadCSVFiles(File folder){
  if (folder.isDirectory()) {
    File[] files = folder.listFiles();
    for (File file : files) {
      println(file);
      pointLists.add(0,importCsvAsPVectorList(file));   
    }
  } else {
    println("Ordner nicht gefunden!");
  }
}


/**
 * Transforms the coordinate system so that the origin (0,0)
 * is at the lower-left corner instead of the upper-left.
 *
 * Applies a vertical flip and adjusts the Y translation accordingly.
*/
void adjustCoordinateSystem(){
  pushMatrix();     
  scale(1, -1);
  translate(0, -height);
}


/**
  *Reads the number of bits and dimensions for the current hilbert curve from the file names of the input folder
  @param folder The folder containing CSV files used for the animation
*/
void setNumberOfBitsAndDimensions(File folder){
  int numberOfBits = 0;
  int numberOfDims = 0;
  if (folder.isDirectory()) {
    File[] files = folder.listFiles();
    for (File file : files) {
      println(file);
      String fileName =  file.getName();
      int bits = Character.getNumericValue(fileName.charAt(0));
      int dims = Character.getNumericValue(fileName.charAt(2));
      if(bits > numberOfBits){
        numberOfBits =  bits;
      }
      if(dims > numberOfDims){
        numberOfDims = dims;
      }
    }
  } else {
    println("Ordner nicht gefunden!");
  }
  
  NUMBER_OF_BITS =numberOfBits;
  NUMBER_OF_DIMENSIONS =numberOfDims;
}


/**
  *Since the hilbert curve plotted on a e.g. 4x4 grad is very small, it needs to be scaled a bit.
  *The scalingFactor is computed in such a way, so that fills the given window completely (execept a small border)
*/
void setHCScalingFactor(){
   int unscaledSideLength = int(pow(2,NUMBER_OF_BITS))-1; //2^nBits points, bit 2^nBits -1 gaps. Can still be not perfect, due to rounding errors
   int scalingFactor = (PLOT_WIDTH - 2 * HC_BORDER_SIZE)/unscaledSideLength;
   HC_SCALING_FACTOR = scalingFactor;
}
