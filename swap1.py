int () {
    int a = 5, b = 10, c = 15;

    
    a = a + b + c;
    b = a - (b + c);
    c = a - (b + c);
    a = a - (b + c);

    printf("a = %d\nb = %d\nc = %d", a, b, c);

    return 0;
}