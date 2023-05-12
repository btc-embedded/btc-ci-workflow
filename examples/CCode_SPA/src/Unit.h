#define NULL 0
#define AR_SIZE 10

//Type definition of structure grouping the arrays
typedef struct {
	int * n;
	const volatile int array1[AR_SIZE];
	const volatile int array2[AR_SIZE];
} t_stData;

//Type definition of Enumeration for Array selection
typedef enum {
	PICK_ARRAY1 = 1,
	PICK_ARRAY2,
} t_enumSelect;

//Structure to store operations results
typedef struct {
	char resAdd;
	char resMul;
	char resAv;
} t_stRes;

//Function declaration
t_stRes sub_func(t_enumSelect enSelArrArg, t_stData *stDataArg) ;

//Declaration of operation functions
extern int add (int n, const volatile int *arr);
extern int mul (int n, const volatile int *arr);
extern int average (int n, const volatile int *arr);
