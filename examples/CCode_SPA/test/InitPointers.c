/************* Header-file includes *************/

#ifdef BTC_POINTER_INITIALIZATION_USE_ORIGINAL_HEADER
#include ".\Unit.h"
#else
#include "InitPointers_Typedef.h"
#endif


/***** Argument Variables for Function "sub_func" *****/
/***** .\Unit.c, line 24 *****/

/************* Argument Variable for Parameter "stDataArg" *************/
static int sub_func_BTC_AUTO_stDataArg_n_inst_stub;
t_stData sub_func_BTC_AUTO_stDataArg = {&sub_func_BTC_AUTO_stDataArg_n_inst_stub, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

/***** Pointer Variables to initialize *****/
extern t_stData stDataGlb;

/***** Pointer Initialization Instance Variables *****/
static int ptInststDataGlb_n;

/***** Pointer Initialization for Function "unit" *****/
/***** .\Unit.c, line 17 *****/
void btc_init_pointer_unit(void)
{
   stDataGlb.n = &ptInststDataGlb_n;
}

