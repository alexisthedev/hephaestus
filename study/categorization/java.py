from bug import JavaBug
import categories as ct
import characteristics as pc
import symptoms as sy
import root_causes as rc
# Rename pc.FunctionApi() to pc.FunctionApi() because An informative annotation type used to indicate that an interface type declaration is intended to be a functional interface as defined by the Java Language Specification. Conceptually, a functional interface has exactly one abstract method

java_iter1 = [
    JavaBug(
        "1.JDK-8258972",
        [pc.ParameterizedClasses(),
         pc.ParameterizedTypes(),
         pc.SealedClasses(),
         pc.NestedClasses(),
         pc.Subtyping()
         ],
         True,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.TypeComparison(),
        # 12
        9
    ),
    JavaBug(
        "2.JDK-8254557",
        [pc.Streams(), pc.FunctionAPI(),
         pc.ParameterizedFunctions(), pc.AnonymousClass(),
         pc.Lambdas(), pc.Conditionals(), pc.Reflection(),
         pc.TypeArgsInference(),
         pc.Overriding()
         ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.TypeExpression(),
        # 58
        34
    ),
     JavaBug(
        "3.JDK-8244559",
        [pc.Collections(), pc.Streams(),
         pc.Inline(), pc.NestedClasses(),
         pc.ParameterizedClasses(), pc.ParameterizedTypes(),
         pc.ReferenceTypes(), pc.Lambdas()
         ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Transformation(),
        # 21
        17
    ),
        JavaBug(
        "4.JDK-8191802",
        [pc.ParameterizedClasses(), pc.BoundedPolymorphism(),
         pc.ParameterizedTypes(), pc.UseVariance(),
         pc.Subtyping(), pc.VarTypeInference()
         ],
         True,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.Inference(),
        # 9
        8
    ),
    JavaBug(
        "5.JDK-8231461",
        [pc.FunctionReferences(),
         pc.StaticMethod(), pc.Overloading(),
         ],
         True,
         sy.CompileTimeError(),
         rc.MissingCase(),
        ct.Resolution(),
        # 10
        8
    ),
    JavaBug(
        "6.JDK-8012238",
        [pc.Overriding(),
         pc.Reflection(),
         pc.ParameterizedFunctions(),
         pc.TypeArgsInference(),
         pc.BoundedPolymorphism(),
         pc.ParameterizedTypes()
         ],
         True,
         sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Inference(),
        18
    ),
    JavaBug(
        "7.JDK-8006749",
        [pc.SAM(),
         pc.Lambdas(), pc.ParamTypeInference()
         ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeExpression(),
        # 7
        6
    ),
   JavaBug(
        "8.JDK-6995200",
        [
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.PrimitiveTypes(), pc.ParameterizedTypes()
         ],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        # 9
        8
    ),
    JavaBug(
        "9.JDK-7040883",
        [
            pc.ParameterizedFunctions(), pc.Arrays(),
            pc.TypeArgsInference(),
            pc.Reflection(), pc.ParameterizedTypes()
         ],
         True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Inference(),
        # 16
        6
    ),
    JavaBug(
        "10.JDK-8029721",
        [
            pc.TypeAnnotations(),
            pc.SAM(),
            pc.Lambdas()
        ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectComputation(),
        ct.Environment(),
        # 10
        9
    ),
    JavaBug(
        "11.JDK-8129214",
        [pc.Import(), pc.TypeArgsInference(),
         pc.ParameterizedFunctions(), pc.BoundedPolymorphism()
         ],
        True,
         sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        # 13
        10
    ),
    JavaBug(
        "12.JDK-8203277",
        [pc.Collections(), pc.FunctionAPI(),
         pc.Overriding(), pc.Lambdas(), pc.TypeArgsInference()
         ],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.TypeExpression(),
        # 12
        9
    ),
    JavaBug(
        "13.JDK-8195598",
        [
            pc.ParameterizedFunctions(), pc.Overloading(),
            pc.TypeArgsInference(),
            pc.Lambdas(), pc.FunctionAPI()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Resolution(),
        14,
    ),
    JavaBug(
        "14.JDK-8202597",
        [pc.Cast(),
         pc.Subtyping(),
         pc.FunctionReferences(), pc.IntersectionTypes()
         ],
        True,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.Approximation(),
        # 10
        9
    ),
    JavaBug(
        "15.JDK-8144832",
        [
            pc.ParameterizedClasses(), pc.Cast(), pc.PrimitiveTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        5
    ),
    JavaBug(
        "16.JDK-8169091",
        [
            pc.IntersectionTypes(),
            pc.ParameterizedFunctions(), pc.UseVariance(),
            pc.ParameterizedTypes(), pc.BoundedPolymorphism(),
            pc.TypeArgsInference(),
            pc.Collections(),
            pc.Cast(), pc.StaticMethod(), pc.FunctionReferences()
        ],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.TypeComparison(),
        # 17
        7
    ),
  JavaBug(
        "17.JDK-6996914",
        [
            pc.NestedClasses(), pc.Subtyping(), pc.ParameterizedClasses(),
            pc.TypeArgsInference(), pc.AccessModifiers()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Environment(),
        # 19
        8
    ),
 JavaBug(
        "18.JDK-8154180",
        [
            pc.FunctionAPI(),
            pc.ParameterizedTypes(),
            pc.Lambdas(),
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Resolution(),
        # 15,17
        16
    ),
    JavaBug(
        "19.JDK-7041019",
        [pc.Arrays(), pc.ParameterizedClasses(),
        pc.BoundedPolymorphism(), pc.ParameterizedTypes(),
        pc.Overriding(), pc.Subtyping()
        ],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.WrongParams(),
        ct.Inference(),
        # 24
        8
    ),
    JavaBug(
        "20.JDK-8148354",
        [
            pc.FunctionAPI(),
            pc.FunctionReferences(),
            pc.TypeArgsInference(),
            pc.ParameterizedFunctions(), pc.BoundedPolymorphism(),
            pc.ParameterizedTypes(),
            pc.IntersectionTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Approximation(),
        # 17
        8
    ),
]


java_iter2 = [
    # Note: I see  Bounded Polymorphism characteristic is common in java bugs (18/60) approximately 30% frequency , maybe consider it for paper section about java bugs
    JavaBug(
        "1.JDK-8152832",  # regression
        [
            pc.FunctionReferences(),
            pc.Streams(), pc.Collections(), pc.Lambdas(),
            pc.FunctionAPI(), pc.BoundedPolymorphism(),
            pc.UseVariance(), pc.ParameterizedTypes(),
            pc.TypeArgsInference(),
            pc.ParameterizedClasses(), pc.ParameterizedFunctions(),
            pc.Subtyping()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),  # Contraint solving
        19
    ),
    JavaBug(
        "2.JDK-7042566",
        [
            pc.Overloading(), pc.Varargs()
        ],
        True,
        sy.CompileTimeError(),
        rc.AlgorithmImproperlyImplemented(),
        ct.Resolution(),
        8
    ),
    JavaBug(
        "3.JDK-6476118",
        # no pc.ParameterizedClasses() in test case, but if we consider the declaration of Comparable<T> part of test case its also pc.SAM() , pc.Inheritance(),
        [
            pc.Overriding(), pc.Overloading(),
            pc.SAM(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.MissingCase(),
        ct.Resolution(),
        13
    ),
    JavaBug(
        # regression bug (This is a regression, the code was providing the right error message in JDK 7.)
        "4.JDK-8029569",
        [pc.Varargs(), pc.Overloading()],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectDataType(),
        ct.Resolution(),
        8
    ),
    JavaBug(
        # regression bug
        "5.JDK-8075793",
        [
            pc.Collections(), pc.ParameterizedFunctions(),
            pc.UseVariance(), pc.ParameterizedTypes(),
            pc.Subtyping(),
            pc.TypeArgsInference()
        ],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.Inference(),  # constraint solving
        6
    ),
    JavaBug(
        "6.JDK-8016081",
        [pc.TypeAnnotations(), pc.Lambdas(), pc.Conditionals(), pc.SAM()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Environment(),
        5
    ),
    JavaBug(
        "7.JDK-8226510",
        [pc.Conditionals(), pc.TryCatch()],
        False,
        sy.Runtime(),
        rc.MissingCase(),
        ct.OtherSemanticChecking(),
        10
    ),
    JavaBug(
        "8.JDK-8039214",
        [
            pc.ParameterizedClasses(), pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.ParameterizedTypes(), pc.UseVariance(),
            pc.Inheritance(), pc.Subtyping()
        ],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.TypeComparison(),
        7
    ),
    JavaBug(
        "9.JDK-8029017",
        [pc.TypeAnnotations()],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.TypeComparison(),
        10
    ),
    JavaBug(
        # regression bug
        "10.JDK-7041730",
        [pc.Cast()],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.IncorrectComputation(),
        ct.TypeComparison(),
        3
    ),
    JavaBug(
        "11.JDK-8020804",
        [
            pc.FunctionAPI(),
            pc.ParameterizedClasses(), pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.Arrays(), pc.BoundedPolymorphism(),
            pc.ParameterizedTypes(), pc.Overloading(),
            pc.SAM(), pc.Collections(),
            pc.FunctionReferences()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        12
    ),
    JavaBug(
        "12.JDK-7062745",  # regression
        [
            pc.Overloading(), pc.Collections(),
            pc.Inheritance(), pc.ParameterizedTypes(),
            pc.Subtyping()
        ],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.Resolution(),
        9
    ),
    JavaBug(
        "13.JDK-8189838",
        [
            pc.FBounded(),
            pc.BoundedPolymorphism(), pc.ParameterizedClasses(),
            pc.Collections(), pc.ParameterizedTypes(),
            pc.TypeArgsInference(), pc.IntersectionTypes()
        ],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Approximation(),
        5
    ),
    JavaBug(
        "14.JDK-8011376",
        [
            pc.Lambdas(), pc.TryCatch(), pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.ParameterizedTypes(), pc.Subtyping()
        ],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.OtherSemanticChecking(),
        6
    ),
    JavaBug(
        "15.JDK-8008537",
        [pc.FunctionReferences(), pc.Overloading(), pc.Subtyping()],
        False,
        sy.Runtime(),
        rc.MissingCase(),
        ct.OtherSemanticChecking(),
        17
    ),
    JavaBug(
        "16.JDK-8188144",  # regression
        [pc.ParameterizedTypes(), pc.FunctionReferences(), pc.FunctionAPI()],
        True,
        sy.Runtime(sy.WrongResult()),
        rc.IncorrectComputation(), # MissingCase
        ct.Resolution(),
        9
    ),
    JavaBug(
        # regression
        "17.JDK-8171993",
        [
            pc.ParameterizedTypes(),
            pc.BoundedPolymorphism(),
            pc.Varargs(), pc.TypeArgsInference(), pc.ParameterizedClasses(),
            pc.FunctionReferences(), pc.FunctionAPI()
        ],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Transformation(),
        9
    ),
    JavaBug(
        "18.JDK-8010303",
        # pc.SAM() (Func interface)
        [pc.ParameterizedFunctions(), pc.ParameterizedClasses(),
         pc.TypeArgsInference(),
         pc.ParameterizedTypes(), pc.SAM()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Inference(),
        10
    ),
    JavaBug(
        # regression bug
        "19.JDK-6835428",
        [
            pc.FBounded(),
            pc.UseVariance(), pc.Subtyping(),
            pc.ParameterizedFunctions(), pc.Collections(),
            pc.TypeArgsInference(),
            pc.BoundedPolymorphism()
        ],
        True,
        sy.CompileTimeError(),
        rc.ExtraneousComputation(),
        ct.Inference(),  # constraint solving
        7
    ),
    JavaBug(
        "20.JDK-8029002",
        [
            pc.ParameterizedClasses(), pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.BoundedPolymorphism(), pc.UseVariance(),
            pc.Subtyping(), pc.Inheritance(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),  # constraint solving
        11
    )
]

java_iter3 = [
    JavaBug(
        # regression bug
        # the attached source file takes the javac 2s to compile on JDK 7u45. It takes 80s on JDK 8.
        "1.JDK-8031967",
        #  pc.StandardLibrary?, pc.PrimitiveTypes(),
        [
            pc.Overloading(),
        ],
        True,
        sy.CompilationPerformance(),
        rc.AlgorithmImproperlyImplemented(),
        ct.Resolution(),
        105
    ),
    JavaBug(
        # regression bug
        "2.JDK-6880344",
        # no pc.ParameterziedTypes()
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.Inheritance(),
            pc.BoundedPolymorphism(),
            pc.FBounded()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        9
    ),
    JavaBug(
        "3.JDK-7142086",
        [
            pc.Overloading(),
            pc.Overriding()
        ],
        True,
        sy.CompilationPerformance(),
        # maybe  rc.AlgorithmImproperlyImplemented()
        # algorithm not implemented effectively
        rc.IncorrectComputation(),
        ct.Declarations(),
        84
    ),
    JavaBug(
        "4.JDK-8131915",
        [
            pc.TypeAnnotations(),
            pc.Import()
        ],
        False,
        sy.InternalCompilerError(),
        rc.WrongDataReference(),
        ct.Environment(),
        55
    ),
    JavaBug(
        # regression bug
        "5.JDK-7148242",
        # pc.ParameterizedFunctions() no pc.ParameterizedTypes() test is parameterized function not type?(diesnt have a distinct parameterized type)
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.NestedClasses(),
            pc.BoundedPolymorphism()
        ],
        True,
        sy.CompileTimeError(),
        rc.ExtraneousComputation(),
        # ct.TypeComparison() We see in the fix changes in subtyping(checking whether a type is subtype of another), also we change the creation of bounds
        ct.Declarations(),
        7
    ),
    JavaBug(
        "6.JDK-7020043",
        [
            pc.TypeArgsInference()
        ],
        False,
        # maybe sy.Runtime(sy.ClassCastException)
        sy.Runtime(),
        rc.MissingCase(),
        # ct.Declarations() diamond operator is used on a declaration
        ct.OtherSemanticChecking(),
        5
    ),
    JavaBug(
        "7.JDK-8209173",
        # pc.Collections() (List)
        [
            pc.JavaInterop(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.InternalCompilerError(),
        rc.WrongDataReference(),
        ct.ErrorReporting(),
        62
    ),
    JavaBug(
        # regression bug
        "8.JDK-7181578",
        [
            pc.TryCatch(),
            pc.Conditionals(),
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectSequence(),
        ct.OtherSemanticChecking(),
        16
    ),
    JavaBug(
        "9.JDK-8177933",
        [
            #  pc.StandardFeatures()
        ],
        True,
        sy.InternalCompilerError(),
        rc.ExtraneousComputation(),
        ct.TypeExpression(),
        46
    ),
    JavaBug(
        "10.JDK-8013394",
        [
            pc.Collections(),
            pc.ParameterizedClasses(),
            pc.Inheritance(),
            pc.ParameterizedTypes(),
            pc.Loops()
        ],
        True,
        sy.CompileTimeError(),
        # rc.WrongParams() There is a bug, because the implementation passes insufficient parameters to a method.
        rc.MissingCase(),
        # agreed, maybe consider ct.TypeComparsion()
        #  types.asSuper(iterator.type.getReturnType(), syms.iteratorType.tsym)
        ct.Transformation(),
        27
    ),
    JavaBug(
        "11.JDK-8027253",
        [
            pc.ParameterizedClasses(),
            pc.BoundedPolymorphism(),
            pc.Arrays()
        ],
        False,
        sy.Runtime(sy.WrongResult()),
        rc.FunctionalSpecificationMismatch(),
        # I think it is type-related. Summary: Backing out change allowing arrays in intersection types
        # ct.Approximation()
        ct.Declarations(),
        1
    ),
    JavaBug(
        # regression bug
        "12.JDK-8236546",
        # no pc.Subtyping()?
        [
            pc.Conditionals(),
            pc.Subtyping()
        ],
        # True (EXPECTED BEHAVIOR -Compile normally.)
        False,
        sy.InternalCompilerError(),
        # maybe create a new Logic Error called rc.WrongMethod()
        # The type of the bug is a Wrong Method Called.
        rc.IncorrectCondition(),
        ct.TypeExpression(),
        7
    ),
    JavaBug(
        "13.JDK-8175790",
        [
            pc.ParameterizedFunctions(),
            pc.FunctionAPI(),
            pc.Collections(),
            pc.Subtyping(),
            pc.UseVariance(),
            pc.TypeArgsInference(),
            pc.ParameterizedTypes(),
            pc.Lambdas()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        # ct.Transformation()
        # There is a post attribution visitor that sets default values to null fields in the ASTs.
        # This is not being done for field JCVariableDecl.vartype,
        # so if there is an error during the attribution of a given expression and that field remains null,
        # then NPE can happen during further analysis of the ASTs
        ct.ErrorReporting(),
        26
    ),
    JavaBug(
        # regression bug
        # see first comment. Maybe make a section in the study for asSuper method?
        "14.JDK-8069265",
        # pc.NestedClasses() An interface declared inside a Class
        [
            pc.Collections(),
            pc.ParameterizedTypes(),
            pc.TypeArgsInference(),
            pc.WildCardType(), #TODO
            pc.Cast()
        ],
        True,
        sy.Runtime(sy.ClassCastException()),
        rc.DesignIssue(),
        ct.Approximation(),
        14
    ),
    JavaBug(
        "15.JDK-8009131",
        [
            pc.Lambdas(),
            pc.SAM(),
            pc.ParamTypeInference(),
            pc.Overloading()
        ],
        False,
        sy.Runtime(sy.WrongResult()),
        rc.InsufficientAlgorithmImplementation(),
        # agreed with both, its a type check of exrpession,
        # but its purpose is to  make enclosing overload resolution fail so I think
        # ct.Resolution()
        ct.Resolution(), # TypeExpression
        11
    ),
    JavaBug(
        "16.JDK-8211102",
        # pc.NestedClasses()
        [
            pc.Collections(),
            pc.TypeArgsInference(),
            pc.Overriding(),
            pc.ParameterizedTypes(),
            pc.AnonymousClass(),
            pc.Conditionals()
        ],
        True,
        sy.InternalCompilerError(),
        # rc.ExtraneousComputation()
        # disabling analyzers that cannot run in the given source level
        rc.MissingCase(),
        ct.OtherSemanticChecking(),
        7
    ),
    JavaBug(
        # regression bug
        "17.JDK-8161383",
        # pc.PrimitiveTypes()
        [
            pc.NestedClasses(),
            pc.AugmentedAssignmentOperator(), #TODO
            pc.Inheritance(),
            pc.AccessModifiers()
        ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectComputation(),
        ct.Resolution(),
        11
    ),
    JavaBug(
        "18.JDK-7020657",
        [
            pc.Collections(),
            pc.ParameterizedTypes(),
            pc.MultipleImplements(),
            pc.Overriding()
        ],
        True,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.Declarations(),
        13
    ),
    JavaBug(
        "19.JDK-8034048",
        [
            pc.FunctionReferences(),
            pc.Varargs(),
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.FunctionAPI()
        ],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Approximation(),
        5
    ),
    JavaBug(
        "20.JDK-8173456",
        [
            pc.FunctionAPI(),
            pc.ParameterizedTypes(),
            pc.AccessModifiers(),
            pc.Inheritance(),
            pc.FunctionReferences(),
            pc.NestedClasses()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Resolution(),
        23
    ),
]

java_iter4 = [
    JavaBug(
        "1.JDK-6680106",
        [
            pc.ParameterizedClasses(),
            pc.Arrays(),
            pc.BoundedPolymorphism()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        #maybe consider ct.Declaration() semantic check of a declaration with a bounded type to an array ((b.isErroneous()) set a bound)
        ct.ErrorReporting(),
        2
    ),
    JavaBug(
        "2.JDK-8020147",
        # pc.Cast()(String)i,
        [
            pc.SAM(),
            pc.ParameterizedTypes(),
            pc.ParamTypeInference(),
            pc.TypeArgsInference(),
            pc.ParameterizedClasses(),
            pc.ParameterizedFunctions(),
            pc.Lambdas()
        ],
        True,
        sy.CompileTimeError(),
        # rc.IncorrectSequence() some code from line 10 to 31 is moved to line 49 which changes the sequence of the program execution
        rc.IncorrectComputation(),
        ct.Environment(),
        13
    ),
    JavaBug(
        "3.JDK-8174249",
        # regression bug
        [
            pc.Collections(),
            pc.UseVariance(),
            pc.Reflection(),
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Approximation(),
        18
    ),
    JavaBug(
        "4.JDK-8022508",
        [
            pc.ParameterizedClasses(),
            pc.Inheritance(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.InternalCompilerError(),
        rc.WrongDataReference(),
        ct.Declarations(),
        5
    ),
    JavaBug(
        # regression bug
        "5.JDK-6975231",
        [
            pc.TypeAnnotations()
        ],
        False,
        sy.MisleadingReport(),
        rc.WrongDataReference(),
        ct.ErrorReporting(),
        7
    ),
    JavaBug(
        "6.JDK-8008539",
        [
            pc.SAM(),
            pc.FunctionReferences()
        ],
        False,
        sy.MisleadingReport(),
        rc.MissingCase(),
        ct.ErrorReporting(),
        7
    ),
    JavaBug(
        "7.JDK-8030816",
        # pc.ParamTypeInference()
        [
            pc.SAM(),
            pc.Lambdas(),
            pc.AnonymousClass()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        #agreed, maybe ct.Approximation fits better,  dummyMethodType is considered an Approximation type used form the compiler internally.
        ct.ErrorReporting(),
        12
    ),
    JavaBug(
        "8.JDK-8020149",
        [
            pc.Collections(),
            pc.ParameterizedClasses(),
            pc.Inheritance(),
            pc.ParamTypeInference(),
            pc.ParameterizedTypes(),
            pc.FunctionAPI(),
            pc.BoundedPolymorphism(),
            pc.FBounded(),
            pc.SAM(),
            pc.ParameterizedFunctions(),
            pc.Lambdas()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Inference(),
        18
    ),
    JavaBug(
        # regression bug
        "9.JDK-8176714",
        # no pc.ParameterizedTypes(), pc.This()
        [
            pc.FunctionAPI(),
            pc.ParameterizedTypes(),
            pc.Conditionals(),
            pc.FunctionReferences(),
            pc.TypeArgsInference(),
            pc.Overloading(),
            pc.ParameterizedFunctions()
        ],
        True,
        sy.CompileTimeError(),
        rc.AlgorithmImproperlyImplemented(),
        ct.TypeExpression(),
        10
    ),
    JavaBug(
        "10.JDK-7014715",
        [
            pc.NestedClasses()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.ErrorReporting(),
        8
    ),
    JavaBug(
        "11.JDK-7034495",

        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.WildCardType(),
            pc.BoundedPolymorphism(),
            pc.IntersectionTypes()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        11
    ),
    JavaBug(
        # regression bug
        "12.JDK-8044546",
        # pc.Arrays, pc.PrimitiveTypes() (STEPS TO FOLLOW TO REPRODUCE THE PROBLEM:
        # Create a new method in this class, which returns a boolean and takes an array argument.
        [
            pc.Collections(),
            pc.Streams(),
            pc.Lambdas(),
            pc.TypeArgsInference(),
            pc.ParamTypeInference()
        ],
        False,
        sy.InternalCompilerError(),
        rc.AlgorithmImproperlyImplemented(),
        ct.Inference(),
        9
    ),
    JavaBug(
        # regression bug
        "13.JDK-7005095",
        # no pc.ParameterizedFunctions() in minimized test case on fix
        [
            pc.ParameterizedFunctions(),
            pc.ParameterizedClasses(),
            pc.BoundedPolymorphism(),
            pc.ParameterizedTypes(),
            pc.TypeArgsInference(),
            pc.Cast(),
            pc.Inheritance()
        ],
        False,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.TypeComparison(),
        14
    ),
    JavaBug(
        "14.JDK-8009582",
        # pc.FunctionReferences()(HashMap::new ), pc.SAM()(GenericMethodRefImplClassLSI)
        [
            pc.TryCatch(),
            pc.Inheritance(),
            pc.IOAPI(), # TODO
            pc.Cast()
        ],
        True,
        sy.CompileTimeError(),
        # rc.WrongParams()(types.erasure(refSym.owner.type))
        rc.MissingCase(),
        # is types.erasure considered an approximation type ?maybe ct.Approximation
        ct.Transformation(),
        49
    ),
    JavaBug(
        "15.JDK-7196531",
        [
            pc.TypeAnnotations(),
            pc.Arrays()
        ],
        False,
        sy.MisleadingReport(),
        rc.ExtraneousComputation(),
        ct.ErrorReporting(),
        6
    ),
    JavaBug(
        # regression bug
        "16.JDK-8042759",
        # pc.PrimitiveTypes()
        [
            pc.SAM(),
            pc.Conditionals(),
            pc.Lambdas(),
            pc.ParamTypeInference(),
            pc.Overloading()
        ],
        False,
        sy.Runtime(sy.WrongResult()),
        # agreed, also consider  pc.FunctionalSpecificationMismatch() from the description of the problem,
        # where the JLS8 chapter 15.12.2.2 in not followed.
        rc.WrongParams(),
        ct.TypeExpression(),
        34
    ),
    JavaBug(
        "17.JDK-7151070",
        [
            pc.StaticMethod(),
            pc.AccessModifiers(),
            pc.NestedClasses(),
            pc.ParameterizedClasses(),
            pc.Inheritance(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.InternalCompilerError(),
        rc.WrongParams(),
        ct.ErrorReporting(),
        29
    ),
    JavaBug(
        # regression bug
        "18.JDK-8194998",
        [
            pc.SAM(),
            pc.FunctionReferences(),
            pc.Cast(),
            pc.AccessModifiers()
        ],
        False,
        sy.MisleadingReport(),
        rc.WrongParams(),
        ct.ErrorReporting(),
        10
    ),
    JavaBug(
        "19.JDK-8019480",
        [
            pc.ParameterizedClasses(),
            pc.SAM(),
            pc.ParameterizedTypes(),
            pc.Collections(),
            pc.Lambdas(),
            pc.TypeArgsInference()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        # ct.TypeComparsion get upper bound of type variable recursively until we find it,
        #  its a type comparsion recursive functionality
        ct.TypeExpression(),
        21
    ),
    JavaBug(
        "20.JDK-8164399",
        # pc.ParamTypeInference()(() -> compute(() -> {}))
        [
            pc.TryCatch(),
            pc.ParameterizedFunctions(),
            pc.ParameterizedTypes(),
            pc.BoundedPolymorphism(),
            pc.Lambdas(),
            pc.SAM(),
        ],
        False,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.Inference(),
        16
    ),
]
