class Main {
    public static final void main() {
        A a = new A("a");
        a.foo();
    }
}

interface Function1<A1, A2> {
    public A2 apply(A1 a1);
}

class A {
    public final String a;

    public A(String a) {
        this.a = a;
    }

    void foo() {
        Function1<String, String> clos = (i) -> {
            String s = "s";
            return s;
        };
        println(clos.apply(a));
    }
}