import gifAnimation.*;

GifMaker gifExport;

void setupGifExport(){
  gifExport = new GifMaker(this, "3d_animation.gif");
  gifExport.setRepeat(1); 
  gifExport.setQuality(10);
  gifExport.setDelay(10); 
}

void checkFinishExport(){
 if (animationPhase >= pointLists.size()-1) {
    gifExport.finish();
    exit();
  }
}
