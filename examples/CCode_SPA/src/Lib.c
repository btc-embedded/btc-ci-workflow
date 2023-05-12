int add (int n, const volatile int arr[]){
	
	int i, accu = 0;
	for (i=0; i<n; i++){
		accu = accu + (*(arr+i));
	}
	return accu;
}

int mul (int n, const volatile int arr[]){
	
	int i, accu = 1;
	for (i=0; i<n; i++){
		accu = accu * (*(arr+i));
	}
	return accu;
}

/*
int average (int n, const volatile int *arr){
	
	int i, accu = 0;
	for (i=0; i<n;i++){
		accu = accu + (*(arr+i));
	}
	
	return accu/n;
}
*/