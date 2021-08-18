import sys
from pathlib import Path

import brails.modules


#images = Path("_images/classified/").glob("*.png")
#images = [x for x in sys.argv if Path(x).suffix == ".png"]

images = sys.argv[1] # pass directory for nfloor model
classifier = brails.modules.NFloorDetector()#workDir=".tmp")

classifier.predict(images)



