from bug import GroovyBug
import categories as ct
import characteristics as pc
import symptoms as sy
import root_causes as rc



groovy_iter1 = [
    GroovyBug(
        "1.GROOVY-8609",
        [pc.ParameterizedClasses(),
         pc.ParameterizedTypes(),
         pc.BoundedPolymorphism(),
         pc.Collections()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        5
    ),
    GroovyBug(
        "2.GROOVY-7364",
        [pc.ParameterizedClasses(),
         pc.VarTypeInference(),
         pc.NamedArgs()
         ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Resolution(),
        9
        ),
    GroovyBug(
        "3.GROOVY-5217",
        [pc.Lambdas(), pc.FunctionTypes(), pc.Property()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectSequence(),
        ct.Resolution(),
        7
    ),
    GroovyBug(
        "4.GROOVY-7211",
        [pc.ParameterizedClasses(),
         pc.ParameterizedTypes(),
         pc.NamedArgs()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        13
    ),
    GroovyBug(
        "5.GROOVY-9420",
        [pc.Collections(),
         pc.ParameterizedTypes(),
         pc.VarTypeInference(),
         pc.Subtyping()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectDataType(),
        ct.TypeExpression(),
        14
    ),
    GroovyBug(
        "6.GROOVY-5232",
        [pc.Property(), pc.VarTypeInference()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Resolution(),
        9
    ),
    GroovyBug(
        "7.GROOVY-8330",
        [pc.Subtyping(), pc.Inheritance(), pc.Cast()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        7
    ),
    GroovyBug(
        "8.GROOVY-7721",
        [pc.Arrays(), pc.Subtyping(), pc.Overriding(), pc.JavaInterop()],
        True,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.Resolution(),
        13
    ),
    GroovyBug(
        "9.GROOVY-6021",
        [pc.Lambdas(),
         pc.Collections(),
         pc.DelegationAPI(),
         pc.VarTypeInference()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Transformation(), # TODO backend
        12
    ),
    GroovyBug(
        "10.GROOVY-8247",
        [pc.Lambdas(),
         pc.ParamTypeInference(),
         pc.FunctionTypes(),
         pc.SAM()],
        True,
        sy.InternalCompilerError(),
        rc.WrongDataReference(),
        ct.Inference(),
        9
    ),
    GroovyBug(
        "11.GROOVY-7333",
        [pc.FlowTyping(),
         pc.PrimitiveTypes(),
         pc.Arrays(), pc.Subtyping()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        7

    ),
    GroovyBug(
        "12.GROOVY-7987",
        [pc.StaticMethod()],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.MissingCase(),
        ct.OtherSemanticChecking(),
        7
    ),
     GroovyBug(
        "13.GROOVY-8445",
        [pc.Lambdas(), pc.ParamTypeInference(), pc.Streams()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        11
    ),
    GroovyBug(
        "14.GROOVY-7316",
        [pc.ParameterizedFunctions(),
         pc.Collections()],
        True,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.TypeExpression(),
        2
    ),
    GroovyBug(
        "15.GROOVY-7420",
        [pc.PrimitiveTypes(), pc.Overloading()],
        True,
        sy.CompileTimeError(),
        rc.FunctionalSpecificationMismatch(),
        ct.Resolution(),
        10
    ),
 GroovyBug(
        "16.GROOVY-7315",
        [pc.NamedArgs(), pc.NestedDeclaration(), pc.PrimitiveTypes()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.OtherSemanticChecking(),
        9
    ),
    GroovyBug(
        "17.GROOVY-6030",
        [pc.Collections(), pc.Overriding(), pc.Overloading(),
         pc.Subtyping(), pc.Lambdas()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectSequence(),
        ct.Resolution(),
        4
    ),
    GroovyBug(
        "18.GROOVY-7711",
        [pc.Overriding(), pc.Varargs(), pc.Subtyping(), pc.Inheritance()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Resolution(),
        13
    ),
    GroovyBug(
        "19.GROOVY-6119",
        [pc.Collections(), pc.NamedArgs()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Transformation(),
        8
    ),
    GroovyBug(
        "20.GROOVY-8310",
        [pc.ParameterizedTypes(),
         pc.ParameterizedFunctions(),
         pc.Collections(),
         pc.Lambdas(),
         pc.Subtyping()],
        False,
        sy.Runtime(),
        rc.IncorrectCondition(),
        ct.TypeExpression(),
        10
    )
]




groovy_iter2 = [
    GroovyBug(
        "1.GROOVY-6489",
        # pc.Property() It seems the property name "names" causes a problem, pc.This()
        [pc.ParameterizedTypes, pc.JavaInterop(),
         pc.WithMultipleAssignment()
         ],
        True,
        sy.InternalCompilerError(),
        rc.WrongParams(),
        ct.TypeExpression(),
        17
    ),
    GroovyBug(
        "2.Groovy-8686",
        # pc.VarTypeInference()
        [pc.FlowTyping()],
        False,
        sy.Runtime(sy.AbstractMethodError()),
        rc.MissingCase(),
        # agreed, because we pop the temporary type info from context, maybe consider it also a Transformation bug?
        ct.Environment(),
        4
    ),
    GroovyBug(
        "3.Groovy-6415",
        [pc.ParameterizedFunctions()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        # found it hard to chose, both categories fit to me, but I think Environment(type = applyGenericsContext(resolvedMethodGenerics, type);)is more related to the fix and Expression more general so I would say Environment
        ct.Environment(),  # TypeExpression
        12
    ),
    GroovyBug(
        "4.Groovy-8590",
        [pc.PrimitiveTypes(), pc.Cast(), pc.Subtyping()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        # ct.Inference we add an extra check (if we are in a nested method) in order to correctly infer the  type of nested method call
        ct.TypeExpression(),
        7
    ),
    GroovyBug(
        "5.Groovy-6761",
        # pc.WildCardType()
        [pc.ParameterizedFunctions(),
         pc.ParameterizedTypes(),
         pc.UseVariance()
         ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Resolution(),
        8
    ),
    GroovyBug(
        "6.Groovy-6034",
        [pc.PrimitiveTypes()],
        False,  # At the time was false
        sy.Runtime(sy.VerifyError()),
        # rc.MissingCase() they didnt check the assignment of null to boolean correctly (missed 2 checks) which resulted in runtime exception, i cant understand why its a design issue, was the implamantation correct and the problem was on the design?
        rc.DesignIssue(),
        ct.TypeExpression(),
        5
    ),
    GroovyBug(
        "7.Groovy-6195",
        [pc.Collections(), pc.VarTypeInference()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Resolution(),
        7
    ),
    GroovyBug(
        "8.Groovy-5873",
        [pc.Inheritance(), pc.ParameterizedClasses(),
         pc.ParameterizedTypes(), pc.Property()
         ],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Inference(),
        10
    ),
    GroovyBug(
        "9.Groovy-5415",
        # pc.This()
        [pc.JavaInterop(),
         pc.ParameterizedClasses(),
         pc.ParameterizedTypes(),
         pc.ParameterizedFunctions(),
         pc.Reflection()
         ],
        True,
        sy.CompileTimeError(),
        rc.ExtraneousComputation(),
        ct.TypeComparison(),
        11
    ),
    GroovyBug(
        "10.Groovy-9328",
        # pc.Property()
        [pc.AccessModifiers(), pc.AnonymousClass(),
         pc.Overriding()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Environment(),
        14
    ),
    GroovyBug(
        "11.Groovy-5175",
        [pc.Arrays(),
         pc.Subtyping()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        # ct.TypeApproximation()  This is for internal use only. When an argument method is null,
        # we cannot determine its type, so we use this one as a wildcard ( UNKNOWN_PARAMETER_TYPE).
        # in approximation documentation:  A compiler internally may approximate or convert a given type to another
         # type for various reasons. I think this is an approximation type.
        ct.TypeComparison(),
        7
    ),
    GroovyBug(
        # regression bug
        "12.Groovy-7922",
        # pc.MultipleImplements()
        [pc.Overloading(), pc.Inheritance()],
        False,
        sy.Runtime(sy.AmbiguousMethodError()),
        rc.IncorrectComputation(),
        ct.Resolution(),
        9
    ),
    GroovyBug(
        "13.Groovy-6129",
        [pc.Collections(),
         pc.ParameterizedTypes(),
         pc.TypeArgsInference()],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Inference(),
        2
    ),
    GroovyBug(
        "14.Groovy-8090",
        # pc.WithMultipleAssignment()
        [pc.Collections(),
         pc.ParameterizedTypes(),
         pc.ParameterizedFunctions()
         ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        7
    ),
    GroovyBug(
        "15.Groovy-5742",
        [pc.Import(), pc.ParameterizedClasses(),
         pc.FBounded(), pc.ParameterizedFunctions(),
         pc.ParameterizedTypes(), pc.Inheritance()
         ],
        True,
        sy.InternalCompilerError(),
        # rc.InsufficientAlgorithmImplementation()  reimplementation of the placeholder extraction and resolving map
        rc.IncorrectComputation(),
        ct.Inference(),
        12
    ),
    GroovyBug(
        "16.Groovy-7307",
        [pc.Subtyping(),
         pc.ParameterizedFunctions(), pc.BoundedPolymorphism()
         ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        11
    ),
    GroovyBug(
        "17.Groovy-7618",
        [
         pc.Lambdas(),
         pc.ParamTypeInference(),
         pc.SAM()],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Approximation(),
        10
    ),
    GroovyBug(
        "18.Groovy-5580",
        [pc.Inheritance(), pc.Property()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Resolution(),
        14
    ),
    GroovyBug(
        "19.Groovy-7061",
        [pc.Collections(), pc.ParamTypeInference(),
         pc.Lambdas()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Inference(),
        5
    ),
    GroovyBug(
        "20.Groovy-5240",
        [pc.Reflection()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        #it is TypeExpression  but maybe consider ct.Tranformation? change the way we visit expressions.
        ct.TypeExpression(),
        7
    )
]

groovy_iter3 = [
    GroovyBug(
        "1.GROOVY-5411",
        # pc.StaticMethod() (static context)
        [
            #  pc.StandardFeatures()
        ],
        False,
        sy.Runtime(sy.MissingMethodException()),
        rc.MissingCase(),
        ct.OtherSemanticChecking(),
        8
    ),
    GroovyBug(
        "2.GROOVY-8961",
        [pc.Collections(), pc.ParameterizedTypes(), pc.Property()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        6
    ),
    GroovyBug(
        "3.GROOVY-6787",
        [pc.ParameterizedFunctions(),
         pc.TypeArgsInference(),
         pc.BoundedPolymorphism(),
         pc.ParameterizedTypes(),
         pc.Collections()],
        True,
        sy.Runtime(sy.ClassCastException()),
        rc.IncorrectComputation(),
        ct.Inference(),
        11
    ),
    GroovyBug(
        "4.GROOVY-7327",
        # no pc.ParameterizedTypes(), pc.Varargs() (Arrays.asList(sequence)[0..1])
        [pc.JavaInterop(),
         pc.ParameterizedFunctions(),
         pc.Collections(),
         pc.TypeArgsInference(),
         pc.ParameterizedTypes(),
         pc.Arrays(),
         pc.Enums()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        6
    ),
    GroovyBug(
        "5.GROOVY-5332",
        [pc.Collections(), pc.ParameterizedTypes()],
        True,
        sy.CompileTimeError(),
        # pc.IncorrectComputation() fix body of parameterizeArguments method, could be missing case, but I consider it more algorithmic than logic fix.
        rc.MissingCase(), # IncorrectComputation
        ct.Inference(),
        2
    ),
    GroovyBug(
        "6.GROOVY-9327",
        [
            pc.AnonymousClass(),
            pc.Overriding()
        ],
        False,
        sy.Runtime(sy.MissingMethodException()),
        rc.MissingCase(),
        ct.Environment(),
        9
    ),
    GroovyBug(
        "7.GROOVY-6742",
        [
            pc.ParameterizedFunctions(),
            pc.AnonymousClass(),
            pc.ParameterizedTypes(),
            pc.FunctionAPI(),
            pc.TypeArgsInference(),
            pc.Overriding()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        # ct.Resolution Groovy is unable to resolve this Generics use case, change in ResolveVisitor, we find the enclosing method
        # if (innerClassNode.isAnonymous()) {
        # MethodNode enclosingMethod = innerClassNode.getEnclosingMethod();
        # if (null != enclosingMethod) {
        #     resolveGenericsHeader(enclosingMethod.getGenericsTypes());
        ct.Environment(),
        8
    ),
    GroovyBug(
        "8.GROOVY-6504",
        [
            pc.Lambdas(),
            pc.PrimitiveTypes(),
            pc.Collections(),
            pc.TypeArgsInference(),
        ],
        True,
        sy.CompileTimeError(),
        # pc.InsufficientAlgorithmImplementation()
        # algorithmic error not a simple missing case, we can see many methods like fullyResolve or typeCheckMethodArgumentWithGenerics or typeCheckMethodsWithGenerics removed and re-implemented
        #  The fix above refines the implementation of the algorithm related to selecting the correct "inject" method so I think it is pc.InsufficientAlgorithmImplementation()
        rc.MissingCase(),
        # found it difficult, both fit I would say TypeExpression because mostly the fix is related more with the type check of expression than with the process of inferring a type variable.
        # 
        ct.Inference(), # TypeExpression
        1
    ),
    GroovyBug(
        "9.GROOVY-9518",
        # pc.pc.TypeArgsInference()  {foo, bar -> println(bar.size())}) for argument Consumer<String, ? super List<Integer>> bar 
        
        [
            pc.JavaInterop(),
            pc.FunctionAPI(),
            pc.ParameterizedTypes(),
            pc.ParamTypeInference(),
            pc.Collections(),
            pc.Lambdas(),
            pc.UseVariance()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeExpression(),
        28
    ),
    GroovyBug(
        "10.GROOVY-5172",
        # pc.ParamTypeInference() { ->printHtmlPart(2) }
        [
            pc.JavaInterop(),
            pc.Inheritance(),
            pc.PrimitiveTypes(),
            pc.ParameterizedTypes(),
            pc.Lambdas(),
            pc.TypeArgsInference(),
            pc.WildCardType() # TODO
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        11
    ),
    GroovyBug(
        "11.GROOVY-5141",
        #pc.ParamTypeInference()(same as GROOVY-5141 ) maybe create a characterisitc it (implicit variable that is provided in closures.)
        [
            pc.Collections(),
            pc.Lambdas(),
            pc.TypeArgsInference()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Resolution(),
        1
    ),
    GroovyBug(
        "12.GROOVY-5601",
        # pc.SAM()(Mapper<F, T>), no pc.Overriding()
        [
            pc.AnonymousClass(),
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.TypeArgsInference(),
            pc.Overriding()
        ],
        False,
        sy.InternalCompilerError(),
        # rc.MissingCase() we add a check to report an error message
        rc.DesignIssue(),
        # I think it fits in 2 categories.
        # ct.Declaration() because we have a Semantic check of a class declaration, if it is using generics, is inner and is anonymous create an error message.
        # maybe it could also be ct.ErrorReporting()? we add a check to add an errormessage
        # ct.Declaration() fits better
        ct.OtherSemanticChecking(),
        18
    ),
    GroovyBug(
        "13.GROOVY-6757",
        [
            pc.Collections(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        6
    ),
    GroovyBug(
        "14.GROOVY-8629",
        # no pc.ParameterizedClasses(), pc.This(), pc.Property() (in fix we see pushEnclosingPropertyExpression),
        [
            pc.Collections(),
            pc.ParameterizedTypes(),
            pc.NestedDeclaration(),
            pc.ParameterizedClasses(),
            pc.Subtyping(),
            pc.Overriding()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Environment(),
        54
    ),
    GroovyBug(
        "15.GROOVY-5456",
        # pc.PrimitiveTypes(), pc.ParamTypeInference() (only it/2 statement without closure parameters) ({ [closureParameters -> ] statements })
        [
            pc.ArithmeticExpressions(),
            pc.Lambdas(),
        ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.TypeExpression(),
        5
    ),
    GroovyBug(
        "16.GROOVY-8157",
        [
            pc.Inheritance(),
            pc.Subtyping(),
            pc.FlowTyping()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        # the fix fits also ct.TypeComparsion()  if (accessedVariable instanceof Parameter) (((Parameter) accessedVariable) casting)
        # it also fits Environment because putNodeMetaData changes context
        ct.Environment(),
        13
    ),
    GroovyBug(
        "17.GROOVY-5145",
        [
            pc.Collections(),
            pc.TypeArgsInference(),
            pc.ParamTypeInference(),
            pc.Lambdas()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Inference(),
        1
    ),
    GroovyBug(
        "18.GROOVY-6671",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.ParamTypeInference(),
            pc.ParameterizedFunctions(),
            pc.UseVariance(),
            pc.TypeArgsInference(),
            pc.Lambdas(),
            pc.SAM()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        25
    ),
    GroovyBug(
        "19.GROOVY-8319",
        [
            pc.Arrays(),
            pc.VarTypeInference()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Environment(),
        4
    ),
    GroovyBug(
        "20.GROOVY-7880",
        # pc.This()
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.TypeArgsInference()
        ],
        True,
        sy.InternalCompilerError(),
        rc.WrongDataReference(),
        ct.Inference(),
        27
    )
]
