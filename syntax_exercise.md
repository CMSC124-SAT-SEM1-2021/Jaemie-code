<start> -> begin <block> end
<block> -> <statement>; | <statement> ; <block>
<statement> -> <var> = <expression>
<var> -> A | B | C
<expression> -> <var><operator><var> | <var><operator><expression>|( <expression> )
<operator> ->  +|-|*|/|%
