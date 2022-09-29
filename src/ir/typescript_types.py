from collections import defaultdict

import src.ir.ast as ast
import src.ir.typescript_ast as ts_ast
import src.ir.builtins as bt
import src.ir.types as tp
import src.ir.ast as ast
import src.utils as ut
from src.ir.decorators import two_way_subtyping

class TypeScriptBuiltinFactory(bt.BuiltinFactory):
    def get_language(self):
        return "typescript"

    def get_builtin(self):
        return TypeScriptBuiltin

    def get_void_type(self):
        return VoidType()

    def get_any_type(self):
        return ObjectType()

    def get_number_type(self):
        return NumberType(primitive=False)

    def get_boolean_type(self):
        return BooleanType(primitive=False)

    def get_char_type(self):
        return StringType(primitive=False)

    def get_string_type(self):
        return StringType(primitive=False)

    def get_big_integer_type(self):
        return BigIntegerType(primitive=False)

    def get_array_type(self):
        return ArrayType()

    def get_function_type(self, nr_parameters=0):
        return FunctionType(nr_parameters)

    def get_object_type(self):
        return ObjectLowercaseType()

    def get_primitive_types(self):
        return [
            NumberType(primitive=False),
            StringType(primitive=False),
            SymbolType(primitive=False),
            BooleanType(primitive=False),
            BigIntegerType(primitive=False),
            NullType(primitive=False),
            UndefinedType(primitive=False)
        ]

    def get_integer_type(self):
        return NumberType(primitive=False)

    def get_byte_type(self):
        return NumberType(primitive=False)

    def get_short_type(self):
        return NumberType(primitive=False)

    def get_long_type(self):
        return NumberType(primitive=False)

    def get_float_type(self):
        return NumberType(primitive=False)

    def get_double_type(self):
        return NumberType(primitive=False)

    def get_big_decimal_type(self):
        return NumberType(primitive=False)

    def get_null_type(self):
        return NullType(primitive=False)

    def get_non_nothing_types(self): # Overwriting Parent method to add TS-specific types
        types = super().get_non_nothing_types()
        types.extend([
            self.get_null_type(),
            UndefinedType(primitive=False),
            ] + literal_types.get_literal_types())
        return types

    def get_decl_candidates(self):
        return [gen_type_alias_decl,]

    def update_add_node_to_parent(self):
        return {
            ts_ast.TypeAliasDeclaration: add_type_alias,
        }

    def get_dynamic_types(self, gen_object):
        return [
            union_types.get_union_type(gen_object),
        ]

    def get_constant_candidates(self, constants):
        """ Updates the constant candidates of the generator
        with the type-constant pairs for language-specific features.

        Args:
            gen_object: The generator instance
            constants: The dictionary of constant candidates
                       at the time of the method call
        Returns:
            A dictionary where the keys are strings of type names and
            values are functions that return the appropriate constant
            node for the type.

            The constants dictionary is updated at the generator-side
            with the method's returned key-value pairs.

            This method is called at src.ir.generator.get_generators()

        """
        return {
            "NumberLiteralType": lambda etype: ast.IntegerConstant(etype.literal, NumberLiteralType),
            "StringLiteralType": lambda etype: ast.StringConstant(etype.literal),
            "UnionType": lambda etype: union_types.get_union_constant(etype, constants),
        }


class TypeScriptBuiltin(tp.Builtin):
    def __init__(self, name, primitive):
        super().__init__(name)
        self.primitive = primitive

    def __str__(self):
        if not self.is_primitive():
            return str(self.name) + "(typescript-builtin)"
        return str(self.name).lower() + "(typescript-primitive)"

    def is_primitive(self):
        return self.primitive


class ObjectType(TypeScriptBuiltin):
    def __init__(self, name="Object"):
        super().__init__(name, False)


class ObjectLowercaseType(TypeScriptBuiltin):
    def __init__(self, name="object"):
        super().__init__(name, False)
        self.supertypes.append(ObjectType())


class VoidType(TypeScriptBuiltin):
    def __init__(self, name="void"):
        super().__init__(name, False)
        self.supertypes.append(ObjectType())


class NumberType(TypeScriptBuiltin):
    def __init__(self, name="Number", primitive=False):
        super().__init__(name, primitive)
        self.supertypes.append(ObjectType())

    def box_type(self):
        return NumberType(self.name, primitive=False)

    def get_name(self):
        if self.is_primitive:
            return "number"
        return super().get_name()


class BigIntegerType(TypeScriptBuiltin):
    def __init__(self, name="BigInt", primitive=False):
        super().__init__(name, primitive)
        self.supertypes.append(ObjectType())

    def is_assignable(self, other):
        assignable_types= [BigIntegerType]
        return self.is_subtype(other) or type(other) in assignable_types

    def box_type(self):
        return BigIntegerType(self.name, primitive=False)

    def get_name(self):
        if self.is_primitive:
            return "bigint"
        return super().get_name()


class BooleanType(TypeScriptBuiltin):
    def __init__(self, name="Boolean", primitive=False):
        super().__init__(name, primitive)
        self.supertypes.append(ObjectType())

    def box_type(self):
        return BooleanType(self.name, primitive=False)

    def get_name(self):
        if self.is_primitive:
            return "boolean"
        return super().get_name()


class StringType(TypeScriptBuiltin):
    def __init__(self, name="String", primitive=False):
        super().__init__(name, primitive)
        self.supertypes.append(ObjectType())

    def box_type(self):
        return StringType(self.name, primitive=False)

    def get_name(self):
        if self.is_primitive:
            return "string"
        return super().get_name()


class SymbolType(TypeScriptBuiltin):
    def __init__(self, name="Symbol", primitive=False):
        super().__init__(name, primitive)
        self.supertypes.append(ObjectType())

    def box_type(self):
        return SymbolType(self.name, primitive=False)

    def get_name(self):
        if self.is_primitive():
            return "symbol"
        return super().get_name()


class NullType(ObjectType):
    def __init__(self, name="null", primitive=False):
        super().__init__(name)
        self.primitive = primitive

    def box_type(self):
        return NullType(self.name)

    def get_name(self):
        return 'null'


class UndefinedType(ObjectType):
    def __init__(self, name="undefined", primitive=False):
        super().__init__(name)
        self.primitive = primitive

    def box_type(self):
        return UndefinedType(self.name)

    def get_name(self):
        return 'undefined'


class AliasType(ObjectType):
    def __init__(self, alias, name="AliasType", primitive=False):
        super().__init__()
        self.alias = alias
        self.name = name
        self.primitive = primitive

    def get_type(self):
        return self.alias

    @two_way_subtyping
    def is_subtype(self, other):
        if isinstance(other, AliasType):
            return self.alias.is_subtype(other.alias)
        return self.alias.is_subtype(other)

    def box_type(self):
        return AliasType(self.alias, self.name)

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return (isinstance(other, AliasType) and
                 self.alias == other.alias)

    def __hash__(self):
        return hash(str(self.name) + str(self.alias))


class NumberLiteralType(TypeScriptBuiltin):
    def __init__(self, literal, name="NumberLiteralType", primitive=False):
        super().__init__(name, primitive)
        self.literal = literal
        self.supertypes.append(NumberType())

    def get_literal(self):
        return self.literal

    @two_way_subtyping
    def is_subtype(self, other):
        """ A number literal type is assignable to any
            supertype of type 'number'.

            It is also assignable to other number literal types,
            as long as the other type's literal is the same.

            eg. let num: number
                let litA: 23 = 23
                let litB: 23
                num = litA (correct)
                litB = litA (correct)

            litA is assignable to litB because their literal
            is the same, 23.

        """
        if (isinstance(other, AliasType) and isinstance(other.alias, NumberLiteralType)):
            other = other.alias
        elif isinstance(other, AliasType):
            return isinstance(other.alias, NumberType)

        return ((isinstance(other, NumberLiteralType) and
                  other.get_literal() == self.get_literal()) or
                  isinstance(other, NumberType))

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                 self.name == other.name and
                 self.literal == other.literal)

    def __hash__(self):
        return hash(str(self.name) + str(self.literal))


class StringLiteralType(TypeScriptBuiltin):
    def __init__(self, literal, name="StringLiteralType", primitive=False):
        super().__init__(name, primitive)
        self.literal = literal
        self.supertypes.append(StringType())

    def get_literal(self):
        return '"' + self.literal + '"'

    @two_way_subtyping
    def is_subtype(self, other):
        """ A string literal type is assignable to any
            supertype of type 'string'.

            It is also assignablde to other string literal types,
            as long as the other type's literal is the same.

            eg. let str: string
                let litA: "PULL" = "PULL"
                let litB: "PULL"
                str = litA (correct)
                litB = litA (correct)

            litA is assignable to litB because their literal
            is the same, "PULL".

        """
        if (isinstance(other, AliasType) and isinstance(other.alias, StringLiteralType)):
            other = other.alias
        elif isinstance(other, AliasType):
            return isinstance(other.alias, StringType)

        return ((isinstance(other, StringLiteralType) and
                  other.get_literal() == self.get_literal()) or
                  isinstance(other, StringType))

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                 self.name == other.name and
                 self.literal == other.literal)

    def __hash__(self):
        return hash(str(self.name) + str(self.literal))


class LiteralTypeFactory:
    def __init__(self, str_limit, num_limit):
        self.str_literals = []
        self.num_literals = []
        # Define max number for generated literals
        self.str_limit = str_limit
        self.num_limit = num_limit

    def get_literal_types(self):
        sl = self.gen_string_literal()
        nl = self.gen_number_literal()
        return [sl, nl]

    def gen_string_literal(self):
        lit = None
        if (len(self.str_literals) == 0 or
                (len(self.str_literals) < self.str_limit and
                ut.random.bool())):
            # If the limit for generated literals
            # has not been surpassed, we can randomly
            # generate a new one.
            lit = StringLiteralType(ut.random.word().lower())
            self.str_literals.append(lit)
        else:
            lit = ut.random.choice(self.str_literals)
        return lit

    def gen_number_literal(self):
        lit = None
        if (len(self.num_literals) == 0 or
                (len(self.num_literals) < self.num_limit and
                ut.random.bool())):
            # If the limit for generated literals
            # has not been surpassed, we can randomly
            # generate a new one.
            lit = NumberLiteralType(ut.random.integer(-100, 100))
            self.num_literals.append(lit)
        else:
            lit = ut.random.choice(self.num_literals)
        return lit


class UnionType(TypeScriptBuiltin):
    def __init__(self, types, name="UnionType", primitive=False):
        super().__init__(name, primitive)
        self.types = types

    def get_types(self):
        return self.types

    def is_combound(self):
        return True

    @two_way_subtyping
    def is_subtype(self, other):
        if isinstance(other, UnionType):
            return set(self.types).issubset(other.types)
        return other.name == 'Object'

    def dynamic_subtyping(self, other):
        return other in set(self.types)

    def substitute_type_args(self, type_map,
                             cond=lambda t: t.has_type_variables()):
        new_types = []
        for t in self.types:
            new_t = (t.substitute_type_args(type_map, cond)
                     if t.has_type_variables()
                     else t)
            new_types.append(new_t)
        return UnionType(new_types)

    def has_type_variables(self):
        return any(t.has_type_variables() for t in self.types)

    def get_type_variables(self, factory):
        # This function actually returns a dict of the enclosing type variables
        # along with the set of their bounds.
        type_vars = defaultdict(set)
        for t in self.types:
            if t.is_type_var():
                type_vars[t].add(
                    t.get_bound_rec(factory))
            elif t.is_combound() or t.is_wildcard():
                for k, v in t.get_type_variables(factory).items():
                    type_vars[k].update(v)
            else:
                continue
        return type_vars

    def to_variance_free(self, type_var_map=None):
        new_types = []
        for t in self.types:
            new_types.append(t.to_variance_free(type_var_map)
                             if t.is_combound()
                             else t)
        return UnionType(new_types)

    def to_type_variable_free(self, factory):
        # We translate a union type that contains
        # type variables into a parameterized type that is
        # type variable free.
        new_types = []
        for t in self.types:
            new_types.append(t.to_type_variable_free(factory)
                             if t.is_combound()
                             else t)
        return UnionType(new_types)

    def get_name(self):
        return self.name

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.name == other.name and
                set(self.types) == set(other.types))

    def __hash__(self):
        return hash(str(self.name) + str(self.types))


class UnionTypeFactory:
    def __init__(self, max_ut, max_in_union):
        self.max_ut = max_ut
        self.unions = []
        self.max_in_union = max_in_union

    def get_number_of_types(self):
        return ut.random.integer(2, self.max_in_union)

    def get_types_for_union(self, gen):
        num_of_types = self.get_number_of_types()
        types = set()
        while len(types) < num_of_types:
            t = gen.select_type(exclude_dynamic_types=True)
            types.add(t)
        return list(types)

    def gen_union_type(self, gen):
        """ Generates a union type that consists of N types
            where N is a number in [2, self.max_in_union].

            Args:
                gen - Instance of Hephaestus' generator

        """
        types = self.get_types_for_union(gen)
        gen_union = UnionType(types)
        self.unions.append(gen_union)
        return gen_union

    def get_union_type(self, gen_object):
        """ Returns a previously created union type
            or a newly generated at random.

            If there are previously generated union types
            and they have not exceeded the limit, we make a
            probabilistic choice on whether to pick one of
            the already generated types or create a new one.

        """
        return self.gen_union_type(gen_object)
        generated = len(self.unions)
        if generated == 0:
            return self.gen_union_type(gen_object)
        if generated >= self.max_ut or ut.random.bool():
            return ut.random.choice(self.unions)
        return self.gen_union_type(gen_object)

    def get_union_constant(self, utype, constants):
        """ This method randomly chooses one of the types in a type's
        union and then assigns the union a constant value that matches
        the randomly selected type.

        A union type can have types like 'Object' or 'undefined'
        as part of its union, which however do not have a respective
        constant equivalent.

        Hence, we only consider types that we can generate a constant
        from. If there is none, we revert to a bottom constant.

        TODO revisit this after implementing structural types.

        """
        type_candidates = [t for t in utype.types if t.name in constants]
        if len(type_candidates) == 0:
            return ast.BottomConstant(utype.types[0])
        t = ut.random.choice(type_candidates)
        return constants[t.name](t)


class ArrayType(tp.TypeConstructor, ObjectType):
    def __init__(self, name="Array"):
        # In TypeScript, arrays are covariant.
        super().__init__(name, [tp.TypeParameter(
            "T", variance=tp.Covariant)])


class FunctionType(tp.TypeConstructor, ObjectType):
    def __init__(self, nr_type_parameters: int):
        name = "Function" + str(nr_type_parameters)

        # In Typescript, type parameters are covariant as to the return type
        # and contravariant as to the arguments.

        type_parameters = [
            tp.TypeParameter("A" + str(i), tp.Contravariant)
            for i in range(1, nr_type_parameters + 1)
        ] + [tp.TypeParameter("R", tp.Covariant)]
        self.nr_type_parameters = nr_type_parameters
        super().__init__(name, type_parameters)
        self.supertypes.append(ObjectType())


# Generator Extension

""" The below functions are all passed as candidate
generation functions to the Hephaestus generator
in order for it to be able to work with language-specific
features of typescript.
"""

def gen_type_alias_decl(gen,
                        etype=None) -> ts_ast.TypeAliasDeclaration:
    """ Generate a Type Declaration (Type Alias)

    Args:
       etype: the type(s) that the type alias describes

    Returns:
        An AST node that describes a type alias declaration
        as defined in src.ir.typescript_ast.py

    """
    alias_type = (etype if etype else
                  gen.select_type()
    )
    initial_depth = gen.depth
    gen.depth += 1
    gen.depth = initial_depth
    type_alias_decl = ts_ast.TypeAliasDeclaration(
        name=ut.random.identifier('lower'),
        alias=alias_type
    )
    gen._add_node_to_parent(gen.namespace, type_alias_decl)
    return type_alias_decl

def add_type_alias(gen, namespace, type_name, ta_decl):
    gen.context._add_entity(namespace, 'types', type_name, ta_decl.get_type())
    gen.context._add_entity(namespace, 'decls', type_name, ta_decl)


# Literal Types

# TODO make these limits user-configurable
MAX_STRING_LITERAL_TYPES = 10
MAX_NUM_LITERAL_TYPES = 10
literal_types = LiteralTypeFactory(MAX_STRING_LITERAL_TYPES, MAX_NUM_LITERAL_TYPES)

# Union Types

# TODO make these limits user-configurable
MAX_UNION_TYPES = 10
MAX_TYPES_IN_UNION = 4
union_types = UnionTypeFactory(MAX_UNION_TYPES, MAX_TYPES_IN_UNION)
