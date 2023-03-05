# Case study: Java

## Primitive types and reference types:

### Q1:

- booleanj -> Java.Lang.Boolean

- float -> Java.Lang.Float

- int -> Java.Lang.Integer

### Q2:

from oracle.com

```java
import java.util.ArrayList;
import java.util.List;

public class Unboxing {

    public static void main(String[] args) {
        Integer i = new Integer(-8);

        // 1. Unboxing through method invocation
        int absVal = absoluteValue(i);
        System.out.println("absolute value of " + i + " = " + absVal);

        List<Double> ld = new ArrayList<>();
        ld.add(3.1416);    // Π is autoboxed through method invocation.

        // 2. Unboxing through assignment
        double pi = ld.get(0);
        System.out.println("pi = " + pi);
    }

    public static int absoluteValue(int i) {
        return (i < 0) ? -i : i;
    }
}
```

This autoconversion between the the object wrapper and the primitive type developers dont need to think about it when coding and produce cleaner code.

### Q3:

The advatages of having both is the ability to have (close to) the performance associated with primitive types while also having a standerdized size to put in arrays. A disadvantage of doing it this way is that still some performance is lost and the control developers have over memory is lower.



### Q4:

Java passes parameters by value, this means that passing a primitive as an parameter wont change the primitive variable value. 



### Q5 & Q6:

`s1 == s2` compares by refrence, if s1 and s2 are the same object

`s1.equals(s2)` compares the value of the objects s1 and s2



### Q7:



### Q8:



## Classes and inheritance:

### Q9:

Java solves the problem of ambiguity in multiple inheritance by simply not supporting it . -_- 

### Q10:

The static keyword is synthacticly used by adding `static` at the begining of line where your variable is initialized.  This is pragmaticly added class declarations to allow all instances of that class to share the memory for the static variable. This saves memory compared to all instances having the same instance variable and value but not sharing the memory. 

### Q11:

In java there are public and protected inner classes, these are used to group classes that belong together and make the code more organized.
