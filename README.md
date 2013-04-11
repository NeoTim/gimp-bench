gimp-bench : scripts for benchmarking Gimp 
==========================================

1. Get test data from,
  
   http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/

   http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz

2. Copy flipscale.py to ~/.gimp-2.8/plug-ins/ and do chmod +x ~/.gimp-2.8/plug-ins/flipscale.py

3. Copy fubatchpy.scm to ~/.gimp-2.8/scripts/

4. time gimp -i -b '(call_py_flipscale "pics/*.jpg" 120 150)' -b '(gimp-quit 0)'
 
5. Keep the test data in RAMDISK for more consistent results.

