COMMENT
Since this is an electrode current, positive values of i depolarize the cell
and in the presence of the extracellular mechanism there will be a change
in vext since i is not a transmembrane current but a current injected
directly to the inside of the cell.
ENDCOMMENT

NEURON {
        POINT_PROCESS iTest
        RANGE del, predur, preamp, meddur, posdur, posamp
        ELECTRODE_CURRENT i
}

UNITS {
        (nA) = (nanoamp)
             }

PARAMETER {
        del=5 (ms)
        predur=200 (ms)
        meddur=200 (ms)
        posdur=200 (ms)
        preamp=10 (nA) 
        posamp=-10 (nA)
}

ASSIGNED {
        i (nA)
}

BREAKPOINT {
       at_time(del)
       at_time(del + predur)
       at_time(del + predur + meddur)
       at_time(del + predur + meddur + posdur)

       if (t < del) {
        i=0
      }else{
            if (t < del+predur) {
                i = preamp
            }else{
                if (t < del+predur+meddur){
                    i = 0
                }
                else{
                    if (t < del+predur+meddur+posdur){
                        i = posamp
                    }
                    else{
                        i = 0
                    }
                }
            }
        }
    }
