#VSCleaner
##Name
    vsclean.bat
##Purpose
Assume i'm using Microsoft visual studio IDE , my workspace have a structure like this:


    -workspace
 	-type1
	   -project1
      	 -project1.sln
      	 -project1
           -Debug
              -*.exe
              -*.dll
              -*.tlog
           -Release
              -*.exe
              -*.exp
              -*.pdb
	-project2
	   -main
	   -Debug
	   -Release
	  	-*.exe
	  	-*.ocx
	  	-*.*
	  	-.
	  	-.
	---vscleaner.bat

Which means vscleaner.bat being at the root of workspace. After building and building, run vsclean.bat, all trashes gone.