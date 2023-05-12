/************* Header-file includes *************/

#ifdef BTC_STUBCODE_USE_ORIGINAL_HEADER
#include ".\Unit.h"
#else
#include "StubCode_Typedef.h"
#endif


/************* StubCode for undefined Global Variables *************/


/****** Stub for Variable enSelArrGlb ******/
/****** .\Unit.c, line 10 ******/
t_enumSelect enSelArrGlb;

/****** Stub for Variable arResGlb ******/
/****** .\Unit.c, line 12 ******/
int arResGlb[3];

/****** Stub for Variable stResultsGlb ******/
/****** .\Unit.c, line 14 ******/
t_stRes stResultsGlb;


/************* StubCode for undefined Functions *************/

/****** Stub for Function average ******/
/****** .\Unit.h, line 30 ******/
int average (int n, const volatile int *arr){
	
	int i, accu = 0;
	for (i=0; i<n;i++){
		accu = accu + (*(arr+i));
	}
	
	return accu/n;
}



