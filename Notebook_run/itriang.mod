TITLE itriang.mod 

COMMENT
Since this is an electrode current, positive values of i depolarize the cell
and in the presence of the extracellular mechanism there will be a change
in vext since i is not a transmembrane current but a current injected
directly to the inside of the cell.
ENDCOMMENT

NEURON {
        POINT_PROCESS iTriang
        RANGE del, predur, posdur, posamp, possamp
        ELECTRODE_CURRENT i
}

UNITS {
        (nA) = (nanoamp)
             }

PARAMETER {
        del=10 (ms)
        predur=200 (ms)
        posdur=200 (ms)
        posamp=1 (nA)
		possamp=27(nA)
}

ASSIGNED {
        i (nA)
}

BREAKPOINT {
       at_time(del)
       at_time(del + predur)
       at_time(del + predur + posdur)
       

       if (t < del) {
        i = 0
      }else{
            if (t < del+predur) {
                    i = posamp * (t-del)/predur
                }else{
			if (t < del+predur+posdur){
				i = posamp - ((posamp-possamp) * (t-(del+predur))/posdur)
                    }
                    else{
                        i = 0
                    }
                }
            }
        }
