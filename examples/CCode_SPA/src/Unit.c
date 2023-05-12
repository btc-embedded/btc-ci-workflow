#include "Unit.h"

/********************** Global variables **********************/
t_stData stDataGlb = {
	NULL,     						 //Input#1
	{ 1,  3,  3,  7,  4,  2, 0, 0, 0, 0},  //Calibration#1 
	{-1, -3, -3, -7, -4, -2, 0, 0, 0, 0}   //Calibration#2 
};

extern t_enumSelect enSelArrGlb;  	 //Input#2

extern int arResGlb[3]; 			 //Internal varialble #1

extern t_stRes stResultsGlb;  		 //Output #1, #2, #3

/*********************** Software unit **************************/
void unit(void) {
	
	stResultsGlb = sub_func(enSelArrGlb, &stDataGlb);
	
}

/*********************** Sub function **************************/
t_stRes sub_func(t_enumSelect enSelArrArg, t_stData *stDataArg) {
	
	t_stRes stRes;
	
	//Choose Array, calculate Sum, Product and Average and save in an Array of 3 elements
	switch (enSelArrArg) {
	
		case PICK_ARRAY1:
		
			arResGlb[0] = add(*stDataArg->n, stDataArg->array1);
			arResGlb[1] = mul(*stDataArg->n, stDataArg->array1);
			arResGlb[2] = average(*stDataArg->n, stDataArg->array1);
			break;	
			
		case PICK_ARRAY2:
		
			arResGlb[0] = add(*stDataArg->n, stDataArg->array2);
			arResGlb[1] = mul(*stDataArg->n, stDataArg->array2);
			arResGlb[2] = average(*stDataArg->n, stDataArg->array2);
			break;		
			
		default:
			break;
	}
	
	//Copy resutls to the returned structure
	stRes.resAdd = arResGlb[0];
	stRes.resMul = arResGlb[1];
	stRes.resAv = arResGlb[2];
			
	return stRes;
}
