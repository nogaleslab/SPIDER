#!/bin/csh

foreach file (*ef.box3)

set new=`echo $file | sed -e 's/ef.box3//'`

batchboxer input=${new}ef.mrc dbbox=${new}en.box output=stack_ef.img 

end 
 
