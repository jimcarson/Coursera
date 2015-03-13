>>> S = [Vec({0, 1, 2, 3, 4, 5, 6, 7},{1: one, 2: one, 3: one, 4: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{1: one, 3: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{0: one, 1: one, 3: one, 5: one, 6: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{3: one, 4: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{3: one, 5: one, 6: one})]
>>> B = [Vec({0, 1, 2, 3, 4, 5, 6, 7},{2: one, 4: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{0: one, 1: one, 2: one, 3: one, 4: one, 5: one, 6: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{0: one, 1: one, 2: one, 5: one, 6: one})]

'First need to inject B[0]'

>>> vec2rep(S, B[0])
Vec({0, 1, 2, 3, 4},{0: one, 1: one})

'This shows I can eject S[0] or S[1].  I choose S[0].'

>>> S1=[B[0]]+S[1:]

'Now S1 == [B[0],S[1], S[2],S[3],S[4]]
'Now need to inject B[1].'

>>> vec2rep(S1, B[1])
Vec({0, 1, 2, 3, 4},{0: one, 2: one})

"This shows I need to eject S1[0] or S1[2], but I don't want to eject S1[0] so I eject S1[2]."

>>> S2=[B[0],B[1],S[1]]+S1[3:]

'Now S2 == [B[0], B[1], S[1], S[3], S[4]].
'Finally need to inject B[2].'

>>> vec2rep(S2, B[2])
Vec({0, 1, 2, 3, 4},{1: one, 3: one})

"This shows I need to eject S1[1] or S1[3], but I don't want to eject S1[1] so I eject S1[3]."

>>> S3 = [B[0],B[1],B[2],S[1],S[4]]

'Now S3 has same cardinality as S and includes elements of B.'
'But does it have the same span as S?'
'First check if Span of S+S3 includes vectors not in Span of S, using Dimension Lemma.'

>>> rank(S) < rank(S+S3)
False

'Whew!  Now check if Span of S+S3 includes vectors not in Span of S3.'

>>> rank(S3) < rank(S+S3)
True

"All is good. The sequence of injections/ejections should be: [(B[0],S[0]), (B[1],S[2]), (B[2],S[3])]."
"Let's check that..."

>>> morph(S, B)==[(B[0],S[0]), (B[1],S[2]), (B[2],S[3])]
True

"We would have gotten another valid solution if we ejected S[1] when injecting S[0]."
"This would have led to the following sequence of injections/ejections: [(B[0],S[1]), (B[1],S[2]), (B[2],S[3])]."


