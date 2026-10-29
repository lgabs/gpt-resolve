# Comparação com o gabarito: Poliedro Resolve (ITA 2027, 2ª fase, dia 1 - Matemática)

Nota média: **10.0/10** (10 questão(ões); cada item vale o mesmo dentro da questão).

| Questão | Nota | Itens | Resumo |
| ------- | ---- | ----- | ------ |
| 1 | 10.0 | Questão 1: igual | A resolução e o gabarito concordam. As PAs têm 2a_1 + 9r = 87, razão ímpar entre −9 e 9 e a_1 = (87 − 9r)/2. São 5 PAs crescentes, com r = 1, 3, 5, 7, 9 e a_1 = 39, 30, 21, 12, 3, e as 5 mesmas sequências em ordem decrescente: 10 no total. Uma busca por força bruta confirma que só existem essas 10. A resolução está correta e mais bem justificada que o gabarito, que não explica por que a razão para em 9. A única ambiguidade é se as PAs decrescentes contam separadamente (10 ou 5), e a resolução trata os dois casos. |
| 2 | 10.0 | Questão 2: igual | A resolução está correta e bate com o gabarito do Poliedro: S = ] log₂((√5−1)/2) , 1 [, com os dois extremos excluídos. O enunciado foi conferido no PDF original, e as contas foram verificadas numericamente (extremo esquerdo ≈ −0,6942). O único problema achado está no gabarito: no caso 2 aparece '<' onde deveria ser '>', o que não muda a resposta final. |
| 3 | 10.0 | Valor de r: igual, Comprimento do lado: igual | A resolução e o gabarito do Poliedro concordam nos dois itens: r = 1/16 e lado ℓ = √(4−2√2)/2 = √((2−√2)/2) ≈ 0,54. A transcrição confere com o enunciado original. O raciocínio está completo e correto: z^8 = ri, as raízes formam um octógono regular de raio r^(1/8), a área vale 2√2·R², e o lado sai pela lei dos cossenos. Também verifiquei as contas numericamente. Não há nada a contestar. |
| 4 | 10.0 | Q4 (a e raízes de p): igual | A resolução e o gabarito estão de acordo e ambos estão certos. Com a = −2, p(x) = (x+1)^2(x−2)(x^2+1)(x^2−6x+1), e as raízes são −1 (dupla), 2, ±i e 3±2√2. Conferi todas as contas em Python: as condições de divisibilidade, a divisão por q e a fatoração do quociente recíproco. O único problema é um deslize de sinal na redação do gabarito ("8a+16=0" no lugar de "−8a−16=0"), que não muda nada no resultado. |
| 5 | 10.0 | abscissa de C: igual | A resolução está certa e bate com o gabarito do Poliedro: x_C = 5√3 − 9 ≈ −0,34. Os dois usam o mesmo método. C fica na interseção da elipse dada com a elipse de focos A e B e eixo maior 6, o que leva a x²+18x+6=0, e a raiz −9−5√3 é descartada porque \|x\|≤√3. Conferi o enunciado no PDF e refiz as contas em Python; o perímetro dá 10. As poucas imperfeições são de digitação no gabarito e não afetam a resposta. |
| 6 | 10.0 | Questão 6 (número de sêxtuplas): igual | A resolução está correta e bate com o gabarito do Poliedro: são 235 sêxtuplas. Ela usa N={1,2,...}, como manda a convenção da prova, escalona o sistema de forma reversível e conta corretamente as soluções com estrelas e barras. Uma força bruta em Python também deu 235. Não encontrei nenhum ponto que mereça ser levado a um professor. |
| 7 | 10.0 | Questão 7: igual | A resolução está certa e bate com o gabarito do Poliedro: n ∈ {−6, −4, 6, 8}. Os dois usam o mesmo método: dividem os polinômios, obtêm resto 63 e exigem que (n − 1)² − 28 divida 63. Uma busca exaustiva em Python confirmou o conjunto e os quocientes. O único ponto a notar é a expressão do discriminante, mal escrita no gabarito (provavelmente erro de transcrição), que não afeta a resposta. |
| 8 | 10.0 | a: igual, b: igual | A resolução e o gabarito batem nos dois itens, e ambos estão corretos. a) 0<x≤1 ou 9≤x<10. b) Os lados medem √10 e 3√10, com y=3 e x=1 ou x=9. Refiz as contas e conferi numericamente os lados, a área e a perpendicularidade. A resolução é até mais completa que o gabarito, porque justifica em que lado fica cada vértice e prova que 0<y<6. O gabarito só tem um erro de digitação, sem efeito no resultado: escreve 'x−5y−3=0' no lugar de (x−5)(y−3)=0. |
| 9 | 10.0 | Área da seção: equivalente | A resolução está certa e bate com o gabarito do Poliedro: 10 + 5√3 = 5(2 + √3) ≈ 18,66. Os dois seguem o mesmo caminho. A seção é um trapézio com bases 8 (diagonal maior) e 2 (base média da face oposta). A altura é 2 + √3, metade do apótema 2·tg75°. Conferi em coordenadas e a área do polígono de interseção sai exatamente esse valor. O único problema está na transcrição do gabarito, cujas fórmulas aparecem embaralhadas (por exemplo, '52 + √(3)' no lugar de 5(2 + √3)); a resposta oficial não muda. |
| 10 | 10.0 | único: igual | A resolução está correta e coincide com o gabarito do Poliedro: k = 3. Refiz as contas e chequei numericamente as duas imagens. No 1º quadrante, f vai de ]√2−1, 2−√2] ≈ ]0,414; 0,586], sem inteiros. No 3º quadrante, vai de ]√2+1, 2+√2] ≈ ]2,414; 3,414], e o único inteiro é 3, atingido em x ≈ 3,43. Comparada ao gabarito, a resolução é mais rigorosa: trata os módulos desde o início, discute se o quadrante é aberto ou fechado e mostra explicitamente que 3 é atingido. O gabarito tem pequenas imprecisões de redação, como a falta de módulos na primeira linha e desigualdades estritas e não estritas misturadas, mas nada que altere o resultado. |

## Itens

### Questão 1

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Questão 1 | 2a_1+9r=87, r ímpar com -9 ≤ r ≤ 9, a_1=(87-9r)/2. São 5 PAs crescentes: (39,…,48) r=1; (30,…,57) r=3; (21,…,66) r=5; (12,…,75) r=7; (3,…,84) r=9. As outras 5 são as mesmas em ordem decrescente: r=-1,-3,-5,-7,-9 com a_1=48,57,66,75,84. São 10 PAs no total (5 se a ordem não importar). | 10 PAs: crescentes (39,…,48) r=1; (30,…,57) r=3; (21,…,66) r=5; (12,…,75) r=7; (3,…,84) r=9; e as 5 decrescentes correspondentes (r=-1,-3,-5,-7,-9). | igual | both | As duas listas trazem as mesmas 10 sequências. Testei por força bruta todos os pares (a_1, r) com a_1 ≥ 1 e r inteiro em [-60, 60], exigindo os 10 termos ≥ 1 e soma 435. Saem exatamente 10 PAs, iguais às da resolução e às do gabarito. A resolução é mais completa que o gabarito em três pontos: mostra que r é inteiro (r = a_2 − a_1); justifica r ≤ 9 e r ≥ −9 com as condições a_1 ≥ 1 e a_10 ≥ 1, que são equivalências; e descarta r = 0 pela paridade. O gabarito só lista r = 1, 3, 5, 7, 9 e não justifica por que a lista para em 9. |

### Questão 2

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Questão 2 | S = ] log₂((√5−1)/2) , 1 [ (extremo esquerdo ≈ −0,694) | S = { x ∈ ℝ \| log₂((√5 − 1)/2) < x < 1 } | igual | both | Enunciado conferido no PDF original (p. 2): \|log₂(2^x+2)\| > \|2x\|, igual à transcrição. As duas respostas são o mesmo intervalo aberto. Também conferi numericamente: em uma malha de −5 a 5, a desigualdade vale exatamente em (−0,69424…, 1). Nos dois extremos ocorre igualdade: f(x₀) ≈ 2·10⁻¹⁶ e f(1) = 0, então os dois ficam excluídos. A resolução não separa em casos pelo sinal de x. Ela usa \|a\| < b ⇔ −b < a < b, o que é válido porque b = log₂(2^x+2) > 1 > 0. O gabarito separa em x ≥ 0 e x < 0 e chega ao mesmo conjunto. As fatorações estão corretas nos dois: t³+2t²−1 = (t+1)(t²+t−1) e t²−t−2 = (t−2)(t+1). |

### Questão 3

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Valor de r | r = 1/16 | r = 1/16 | igual | both | z^8 = ri e \|z\| = R = r^(1/8). Área do octógono regular: 2√2·R² = √2, então R² = 1/2 e r = R^8 = 1/16. Conferi numericamente: as raízes satisfazem r + iz^8 = 0 e a área pela fórmula do laço dá √2. |
| Comprimento do lado | ℓ = √((2−√2)/2) = √(4−2√2)/2 ≈ 0,54 | l = √(4 − 2√2)/2 = √((2 − √2)/2) | igual | both | A resolução e o gabarito trazem as mesmas duas formas, que são equivalentes. Lei dos cossenos: ℓ² = 2R²(1 − cos45°) = 1 − √2/2. Conferi numericamente: \|z1 − z0\| ≈ 0,5412, igual nas duas formas. |

### Questão 4

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Q4 (a e raízes de p) | a = −2; p(x) = (x+1)^2 (x−2)(x^2+1)(x^2−6x+1); raízes: −1 (dupla), 2, i, −i, 3+2√2, 3−2√2 | a = −2; raízes: −1 (dupla), 2, i, −i, 3 + 2√2, 3 − 2√2 | igual | both | Refiz as contas: p(−1) = −16 − 8a, p(2) = 170 + 85a e p'(−1) = 32 + 16a. As três se anulam só em a = −2. Com a = −2, o produto (x^3−3x−2)(x^4−6x^3+2x^2−6x+1) dá exatamente [1, −6, −1, 10, 7, 14, 9, −2], que são os coeficientes de p. Também (x^2+1)(x^2−6x+1) = x^4−6x^3+2x^2−6x+1. Substituí numericamente as 7 raízes em p e todas o anulam. A resolução e o gabarito chegam à mesma resposta, e a resolução é até mais completa: ela impõe as três condições de divisibilidade, enquanto o gabarito usa só p(−1)=0 e confirma depois, ao obter resto zero na divisão. |

### Questão 5

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| abscissa de C | x_C = 5√3 − 9 ≈ −0,34 | x = 5√3 − 9 | igual | both | A transcrição bate com o enunciado original (p. 5 do PDF). Refiz a conta: com x=1 na elipse, y=±2, então AB=4 e AC+BC=6. A elipse de focos (1,±2) com a'=3, c'=2 e b'²=5 é (x−1)²/5 + y²/9 = 1, ou seja, 9x²−18x+5y²=36. Fazendo 5·E1 − E2 sai x²+18x+6=0, com raízes x=−9±5√3. Como \|x\|≤√3, só fica x=5√3−9≈−0,3397. Nesse ponto y²=180√3−306≈5,769>0, e no Python o perímetro dá 4+AC+BC=10,000. O ponto também satisfaz as duas equações de elipse. A resolução e o gabarito seguem o mesmo caminho e dão a mesma resposta. |

### Questão 6

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Questão 6 (número de sêxtuplas) | 235 | 235 sêxtuplas | igual | both | A transcrição confere com o original (p. 7 do PDF). O escalonamento está certo: (II)−(I) dá x2+S+x6=22, (III)−2(I) dá S+x6=16, então x2=6 e x1=8−2x6. Como N começa em 1, x6 só pode ser 1, 2 ou 3, o que dá S=15, 14, 13. Contando as soluções com xk≥1: C(14,2)+C(13,2)+C(12,2)=91+78+66=235. O gabarito chega às mesmas contas (P_14^{12,2}=14!/(12!·2!)=91 etc.). Também conferi por força bruta em Python, testando todas as combinações com xi≥1: o resultado é 235. |

### Questão 7

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Questão 7 | n ∈ {−6, −4, 6, 8} (quocientes −10, −30, −10 e 18) | n ∈ {−6, −4, 6, 8} | igual | both | As respostas finais coincidem. Refiz a divisão e chega-se a P(n) = (2n − 1)(n² − 2n − 27) + 63. Então n² − 2n − 27 = (n − 1)² − 28 precisa dividir 63, ou seja, (n − 1)² = 28 + d com d ∈ {±1, ±3, ±7, ±9, ±21, ±63}. Só 25 (d = −3) e 49 (d = 21) são quadrados perfeitos, o que dá n ∈ {6, −4} e n ∈ {8, −6}. Uma busca exaustiva em Python com n de −100000 a 100000 encontrou exatamente {−6, −4, 6, 8}, com quocientes −10, −30, −10 e 18, iguais aos da resolução. O denominador nunca se anula para n inteiro, porque 28 não é quadrado, e a resolução diz isso explicitamente. A tabela, a equivalência do passo 2 e as verificações numéricas estão todas certas. |

### Questão 8

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| a | 0 < x ≤ 1 ou 9 ≤ x < 10 | 0 < x ≤ 1 ou 9 ≤ x < 10 | igual | both | As duas chegam a x(10−x) = y(6−y), com y = BF. Como y(6−y) ∈ ]0,9] para 0<y<6, é preciso ter x(10−x) ≤ 9, ou seja, (x−1)(x−9) ≥ 0. Junto com 0<x<10, isso dá 0<x≤1 ou 9≤x<10. A resolução justifica com mais cuidado do que o gabarito: mostra que H fica em AD e G em CD, prova a recíproca e confere que 0<y<6. O gabarito só exige Δ ≥ 0, mas a conclusão é a mesma. |
| b | Lados √10 e 3√10 (dois de cada), para x = 1 ou x = 9 e y = 3 | Lados 3√10 e √10 | igual | both | Área = 60 − (10−x)y − x(6−y) = 30, o que equivale a (x−5)(y−3) = 0. O valor x=5 fica fora do intervalo do item (a), então y=3 e x(10−x)=9, ou seja, x=1 ou x=9. Para x=1: EF = √(81+9) = 3√10 e FG = √(1+9) = √10. Para x=9 os lados só trocam de posição. Conferi numericamente: o produto dos lados dá 30 e o ângulo é reto. |

### Questão 9

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Área da seção | 10 + 5√3 ≈ 18,66 (trapézio de bases 8 e 2, altura 2 + √3) | 5(2 + √3) | equivalente | both | 10 + 5√3 = 5(2 + √3), então os dois valores coincidem. Refiz a conta. O apótema da face é VM = 2/tg15° = 2·tg75° = 4 + 2√3. A seção é o trapézio com bases AD = 8 e E'F' = EF/2 = 2, formada pela diagonal maior e pela base média da face VEF. A altura é OP = VM/2 = 2 + √3, base média do triângulo VMN. Área = (8+2)/2·(2+√3) = 10 + 5√3. Também conferi em coordenadas (python): com h² = 16 + 16√3, o ângulo do vértice dá π/6. O plano por AD paralelo a VBC corta a pirâmide só nos pontos (±4,0,0) e (±1,−√3,h/2). A área do polígono de interseção dá 18,6603 = 10 + 5√3. O caminho da resolução é o mesmo do gabarito, com justificativas mais completas: explica por que só VBC/VEF servem, mostra que a seção é só o trapézio e que OP é de fato a altura. |

### Questão 10

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| único | k = 3 (no 1º quadrante f ∈ ]√2−1, 2−√2], sem inteiros; no 3º quadrante f ∈ ]√2+1, 2+√2], que só contém o inteiro 3, atingido em x = π + ½·arcsen(26−18√2) ≈ 3,43) | k = 3 | igual | both | Conferi o enunciado na página 10 do PDF original e ele bate com a transcrição. Refiz as contas. Como √(1±cos2x) = √2\|cos x\| e √2\|sen x\|, temos f = (√2−1)(sen x+cos x) no 1º quadrante, cuja imagem é ]0,414; 0,586]. No 3º quadrante, f = −(√2+1)(sen x+cos x), cuja imagem é ]2,414; 3,414]. Numericamente, com 2×10⁶ pontos, obtive mínimo e máximo de 0,41421 e 0,58579 no 1º quadrante e de 2,41421 e 3,41421 no 3º. Também confirmei f(π + ½·arcsen(26−18√2)) = 3,0000. A resolução e o gabarito chegam à mesma resposta, e ela está correta. A resolução é mais rigorosa: usa módulos desde o início, discute se o quadrante é aberto ou fechado e mostra explicitamente que 3 é atingido. |

## Pontos de dúvida

- **Q1** (statement): O enunciado não diz se uma PA e a mesma PA escrita ao contrário contam como uma só. Quem considera só o conjunto dos termos encontra 5; quem considera sequências ordenadas encontra 10. O gabarito e a resolução adotam 10, e a resolução também menciona as 5. Na correção, vale aceitar 10 sequências ou 5 com a observação sobre a ordem.
- **Q1** (key): Na resolução do gabarito, a fórmula da soma aparece como (a_1 + a_10 · 10)/2 e (2a_1 + 9r · 10)/2, sem os parênteses certos. O correto é (a_1 + a_10)·10/2 = 5(2a_1 + 9r). Parece erro de digitação ou de transcrição, porque a equação 2a_1 + 9r = 87 que vem depois está certa. As PAs decrescentes também aparecem coladas numa linha só ("…40,3957,54…"), o que é apenas formatação.
- **Q1** (key): O gabarito não justifica por que a razão para em r = 9. Falta dizer que a_1 = (87 − 9r)/2 ≥ 1 exige r ≤ 9 e que, no caso decrescente, a_10 = (87 + 9r)/2 ≥ 1 exige r ≥ −9. Também não descarta explicitamente a PA constante (r = 0), que é impossível porque r precisa ser ímpar. A resolução cobre esses pontos.
- **Q2** (key): No caso 2 da resolução do gabarito aparece 'log₂(2^x + 2) < −2x', mas o certo é '> −2x'. A conclusão do próprio gabarito usa o sentido correto (2^x + 2 > 2^(−2x)), então deve ser erro de digitação ou de extração do texto, e o resultado não muda. Há também perda de formatação (parênteses e expoentes) em trechos como '2^3x + 2·2^(^2x)−1'.
- **Q2** (solution): A resolução tira o módulo do lado esquerdo e resolve −log₂(2^x+2) < 2x < log₂(2^x+2) direto, sem separar casos pelo sinal de x. Está correto e completo. Também confere a igualdade nos dois extremos e escreve o extremo esquerdo de outra forma, −log₂((1+√5)/2). Nada a corrigir.
- **Q4** (key): Na resolução do gabarito, p(−1) = −1+3a+1−5a−7−7a−9+a vale −8a−16, mas ele escreve "8a + 16 = 0". A equação é a mesma (só os sinais estão trocados) e o valor a = −2 continua certo. É um deslize de digitação ou redação.
- **Q4** (key): O gabarito tira a só de p(−1)=0. Isso não basta para garantir que q divide p, porque também seriam necessários p(2)=0 e p'(−1)=0. A divisibilidade só fica confirmada depois, quando a divisão dá resto nulo. O raciocínio está completo, mas um corretor rigoroso poderia pedir que isso fosse dito explicitamente.
- **Q4** (statement): O enunciado pede apenas as raízes de p(x). O valor a = −2 é um passo intermediário que as duas respostas informam. Isso não muda o veredito.
- **Q5** (key): A resolução do gabarito tem erros de digitação ou de extração que não mudam o resultado: aparece "A = 1,2" sem parênteses, "centro em 1,0" e "(x-1^2)/5" no lugar de (x−1)²/5. A forma expandida 9x²−18x+5y²=36 está correta.
- **Q5** (solution): A resolução fixa A=(1,2) e B=(1,−2) "sem perda de generalidade". Isso é válido, porque trocar A com B não altera o perímetro nem o lugar geométrico de C. A checagem de y²>0 é redundante: qualquer x em [−√3, √3] que satisfaça a quadrática dá um ponto real nas duas elipses. Mesmo assim, ela não está errada.
- **Q7** (key): No gabarito, o discriminante está escrito de forma truncada ou errada: 'n² − 2n − k + 27 = 0' e '∆ = 4 + 4k + 27 = m², m² = 4k + 28'. O certo é n² − 2n − (k + 27) = 0, com ∆ = 4 + 4(k + 27) = 4(k + 28). A conclusão de que k + 28 tem de ser quadrado perfeito está certa, porque 4(k + 28) é quadrado se e só se k + 28 é quadrado. Deve ser um problema de extração do texto, e o resultado não muda.
- **Q8** (key): No item (b), o gabarito escreve 'xy−3x−5y+15 = 0 ⇒ x−5y−3 = 0'. Deveria ser (x−5)(y−3) = 0; os parênteses se perderam na transcrição. Isso não afeta a conclusão (x=5 ou y=3).
- **Q8** (key): No item (a), o gabarito impõe só Δ ≥ 0 e não confere que a raiz y = 3 ± √((x−1)(x−9)) cai em ]0,6[. Isso vale porque (x−1)(x−9) < 9 para 0<x<10, mas o gabarito não diz. A resolução faz essa verificação.
- **Q9** (key): O texto da resolução do gabarito saiu com as fórmulas embaralhadas na transcrição. '(AD + PQOT)/2' deveria ser (AD + PQ)·OT/2. '(8 + 2 · tg75°)/2' deveria ser (8 + 2)·tg75°/2. '52 + √(3)' é 5(2 + √3). A resposta oficial 5(2 + √3) bate com o restante da resolução, então é só um problema de formatação, sem erro de conteúdo.
- **Q9** (statement): O enunciado não diz a qual face lateral a seção é paralela. Só as faces paralelas à diagonal escolhida (VBC ou VEF, para a diagonal AD) permitem um plano que contenha AD. Por simetria, as duas dão seções congruentes. A resolução justifica isso explicitamente; o gabarito só supõe a escolha.
- **Q10** (key): Na simplificação inicial, o gabarito escreve f(x) = √2cos x + √2sen x − sen x − cos x, sem módulos, o que é falso fora do 1º quadrante. No Caso 2, porém, aplica o sinal correto (−√2cos x − √2sen x). A resposta não muda, mas a passagem é imprecisa.
- **Q10** (key): No Caso 1, as desigualdades estão inconsistentes. O gabarito escreve primeiro √2/2 ≤ sen(x+π/4) ≤ 1, depois √2/2 < f/(2−√2) e por fim √2−1 ≤ f. Também usa intervalos fechados (0 ≤ x ≤ π/2), embora os pontos sobre os eixos não pertençam a quadrante nenhum. Isso não afeta a resposta, já que nenhum dos extremos √2±1 e 2±√2 é inteiro.
- **Q10** (key): O gabarito usa a mesma letra k para o inteiro do enunciado e para o período 2kπ, o que pode confundir. Além disso, não verifica explicitamente que f atinge o valor 3. Isso decorre implicitamente da continuidade e da imagem calculada.
