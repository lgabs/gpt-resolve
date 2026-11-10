# Comparação com o gabarito: Poliedro Resolve (ITA 2027, 2ª fase, dia 1 - Matemática)

Nota média: **10.0/10** (10 questão(ões); cada item vale o mesmo dentro da questão).

| Questão | Nota | Itens | Resumo |
| ------- | ---- | ----- | ------ |
| 1 | 10.0 | Q1 (única): igual | A resolução e o gabarito concordam: as PAs têm razão ímpar com \|r\| ≤ 9 e a₁ = (87 − 9r)/2, dando 5 crescentes, (39,…,48), (30,…,57), (21,…,66), (12,…,75) e (3,…,84), mais as 5 decrescentes correspondentes, 10 no total. Confirmei por força bruta em python que existem exatamente essas 10. A resolução é mais completa que o gabarito, porque justifica a paridade, o limite r ≤ 9 e a simetria por inversão. O único reparo, menor, é que ela deixa a contagem final condicional ('5, ou 10 com as decrescentes') em vez de afirmar 10. Ainda assim, lista as 10 explicitamente. Veredito: correta, de acordo com o gabarito. |
| 2 | 10.0 | Questão 2 (conjunto solução de \|log2(2^x+2)\| > \|2x\|): igual | A resolução está correta e bate com o gabarito do Poliedro: S = (log2((√5−1)/2), 1), que também pode ser escrito (−log2((1+√5)/2), 1) ≈ (−0,694; 1). Refiz a solução analiticamente e conferi com uma varredura numérica: o intervalo e a exclusão dos dois extremos estão confirmados. Só há detalhes menores: um sinal '<' trocado na resolução do gabarito (Caso 2), que parece erro de digitação, e uma justificativa mal formulada no Passo 1 da resolução. Nenhum dos dois afeta a resposta. |
| 3 | 10.0 | lado do polígono: igual, valor de r: igual | A resolução está correta e bate com o gabarito do Poliedro nos dois itens: r = 1/16 e lado ℓ = √(4−2√2)/2 = √((2−√2)/2) ≈ 0,541. O caminho é o mesmo do gabarito: De Moivre, octógono regular de raio r^{1/8}, área por 8 triângulos e lado pela lei dos cossenos. A resolução ainda confere o resultado com a fórmula da área do octógono pelo lado. A transcrição do enunciado confere com o PDF original. Conferi raízes, área e lado em Python. |
| 4 | 10.0 | Q4 (valor de a e raízes de p): igual | A resolução está correta e coincide com o gabarito do Poliedro: a = -2, e as raízes são -1 (dupla), 2, ±i e 3±2√2. Refiz a divisão, a fatoração completa e o cálculo de p, p' e s nas raízes de q com aritmética exata. A resolução é até mais completa que o gabarito, porque verifica de forma independente as três condições p(2) = 0, p(-1) = 0 e p'(-1) = 0. Não encontrei erro. |
| 5 | 10.0 | abscissa de C: igual | A resolução está certa e bate com o gabarito do Poliedro: x_C = 5√3 − 9. Os dois seguem o mesmo caminho: C fica na interseção da elipse dada com a elipse de focos A e B e eixo maior 6, o que leva a x²+18x+6=0, e a raiz −9−5√3 é descartada porque cai fora de \|x\|≤√3. Conferi todas as contas em Python, e o perímetro dá 10. Não há erro de matemática em nenhum dos dois, só falhas de formatação na transcrição do gabarito. |
| 6 | 10.0 | Questão 6 (número de sêxtuplas): igual | A resolução está correta e coincide com o gabarito do Poliedro: são 235 sêxtuplas. A redução do sistema dá x2 = 6, x1 = 8 − 2x6 e x3+x4+x5 = 16 − x6, com x6 ∈ {1,2,3}. A contagem por estrelas e barras é 91 + 78 + 66 = 235. Refiz as contas e testei por força bruta em Python, que também deu 235. O enunciado transcrito confere com o PDF original. |
| 7 | 10.0 | Questão 7 (valores inteiros de n): igual | A resolução e o gabarito estão certos e chegam à mesma resposta, n ∈ {−6, −4, 6, 8}. O método é o mesmo nos dois: dividir os polinômios (resto 63), exigir que n²−2n−27 divida 63 e testar quais divisores tornam 28+d um quadrado perfeito (d = −3 e d = 21). A resolução está correta e completa e ainda confere os quocientes. O gabarito tem um erro de digitação sem importância na expressão do discriminante. |
| 8 | 10.0 | a: igual, b: igual | A resolução está certa nos dois itens e coincide com o gabarito do Poliedro. No item a, ambos dão 0 < x ≤ 1 ou 9 ≤ x < 10. No item b, ambos dão lados √10 e 3√10. Refiz as contas e chego ao mesmo resultado, que também conferi numericamente. A resolução é até mais completa: mostra que y fica em (0,6) e verifica o ângulo reto e a área. O gabarito tem só um erro de digitação ('x−5y−3=0' no lugar de (x−5)(y−3)=0), que não afeta a resposta. |
| 9 | 10.0 | Área da seção: igual | A resolução está certa e bate com o gabarito do Poliedro: a área da seção é 5(2+√3) = 10+5√3 ≈ 18,66. Os dois fazem o mesmo caminho. A seção é um trapézio de bases 8 (diagonal maior AD) e 2 (base média PQ = EF/2). A altura é tg75° = 2+√3, ou seja, metade do apótema lateral VM = 2(2+√3). Conferi com uma conta em coordenadas no Python: o ângulo no vértice dá 30°, a seção tem os vértices (±4,0,0) e (±1,−√3,h/2), e a área é 18,660254…, igual a 5(2+√3). A única falha é no texto do gabarito, onde a fórmula final saiu truncada. O valor final do gabarito está certo. |
| 10 | 10.0 | único: igual | A resolução está correta e concorda com o gabarito do Poliedro: k = 3. No 1º quadrante, f percorre (√2−1, 2−√2], intervalo sem inteiros. No 3º quadrante, percorre (√2+1, 2+√2], que contém só o inteiro 3. Confirmei isso numericamente e conferi que o x explícito dado na resolução (≈ 3,429 rad, no 3º quadrante) dá f(x) = 3. A resolução é até mais cuidadosa que o gabarito: usa os módulos corretamente, justifica por continuidade que todos os valores do intervalo são atingidos e trata o caso dos pontos sobre os eixos. O gabarito só tem pequenas imprecisões de redação, como a falta dos módulos numa linha intermediária e a mistura de desigualdades estritas e não estritas, que não afetam a resposta. |

## Itens

### Questão 1

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Q1 (única) | r ímpar, 1 ≤ r ≤ 9, a₁ = (87 − 9r)/2: (39,…,48) r=1; (30,…,57) r=3; (21,…,66) r=5; (12,…,75) r=7; (3,…,84) r=9; mais as 5 invertidas (r = −1, −3, −5, −7, −9). Ao todo 5 PAs crescentes, ou 10 contando as decrescentes. | 10 PAs: as crescentes (39,…,48) r=1; (30,…,57) r=3; (21,…,66) r=5; (12,…,75) r=7; (3,…,84) r=9, e as 5 decrescentes correspondentes (r = −1, −3, −5, −7, −9). | igual | both | Reli o enunciado no PDF original (pág. 1): 'Descreva todas as progressões aritméticas de 10 números naturais cuja soma resulte em 435', com ℕ = {1,2,3,…}. A transcrição está correta. A condição S₁₀ = 5(2a₁+9r) = 435 dá 2a₁ + 9r = 87. Daí r é ímpar, e a exigência de que o menor termo seja ≥ 1 dá \|r\| ≤ 9. Fiz uma busca por força bruta em python (a₁ de 1 a 435, r de −100 a 100) e encontrei exatamente 10 soluções: (a₁,r) = (3,9), (12,7), (21,5), (30,3), (39,1), (48,−1), (57,−3), (66,−5), (75,−7), (84,−9). São exatamente as 10 da resolução e as 10 do gabarito. A resolução descreve as 10 sequências explicitamente (as 5 crescentes e as 5 invertidas, com razões e primeiros termos). Ela só deixa a contagem em aberto ('5 crescentes, ou 10 contando as decrescentes'), enquanto o gabarito afirma 10. Como as sequências invertidas são PAs distintas e válidas, o certo é contar 10, e a resolução de fato as inclui. Por isso o conteúdo coincide. |

### Questão 2

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Questão 2 (conjunto solução de \|log2(2^x+2)\| > \|2x\|) | x ∈ (log2((√5−1)/2), 1) = (−log2((1+√5)/2), 1) ≈ (−0,694; 1) | S = { x ∈ ℝ \| log2((√5 − 1)/2) < x < 1 } | igual | both | Os dois dão o mesmo intervalo aberto, e a resolução também escreve o extremo inferior na forma equivalente −log2(φ), com φ = (1+√5)/2. Refiz a questão. Como 2^x + 2 > 2, o log é maior que 1 e o módulo da esquerda pode ser retirado. Caso x ≥ 0: t² − t − 2 < 0 dá 2^x < 2, ou seja, 0 ≤ x < 1. Caso x < 0: t³ + 2t² − 1 = (t+1)(t² + t − 1) > 0 dá t > (√5−1)/2, ou seja, log2((√5−1)/2) < x < 0. A união é (log2((√5−1)/2), 1). Uma varredura numérica em [−5, 5] com passo 10⁻⁴ deu exatamente [−0,6942; 0,9999], sem buracos, e log2((√5−1)/2) ≈ −0,69424. Nos dois extremos vale a igualdade, então ambos ficam de fora, como os dois textos afirmam. Os valores de teste da resolução (x = −0,69, −0,70, 0,5 e 2) também conferem. |

### Questão 3

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| lado do polígono | ℓ = √((2−√2)/2) = √(4−2√2)/2 ≈ 0,541 | l = √(4 − 2√2)/2 = √((2 − √2)/2) | igual | both | Mesma expressão, escrita nas mesmas duas formas. Conferi numericamente: com r = 1/16, a distância entre raízes vizinhas dá 0,541196, igual a √(4−2√2)/2. |
| valor de r | r = 1/16 | r = 1/16 | igual | both | z^8 = ir dá um octógono regular de raio R = r^{1/8}. A área é 2√2·R² = √2, logo R² = 1/2 e r = R^8 = 1/16. Conferi numericamente que as oito raízes satisfazem r + iz^8 = 0 e que o polígono tem área √2. |

### Questão 4

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Q4 (valor de a e raízes de p) | a = -2; raízes: -1 (dupla), 2, i, -i, 3+2√2, 3-2√2 | a = -2; raízes: -1 (dupla), 2, i, -i, 3+2√2, 3-2√2 | igual | both | Conferi com aritmética exata. O resto de p por q, em função de a, sai proporcional a (a+2): (10+5a)x² + (52+26a)x + (26+13a). Ele só se anula para a = -2. Com a = -2, o quociente é x⁴-6x³+2x²-6x+1, com resto zero. O produto (x+1)²(x-2)(x²+1)(x²-6x+1) reproduz exatamente p(x) = x⁷-6x⁶-x⁵+10x⁴+7x³+14x²+9x-2. Conferi também a resolução: p(2) = 170+85a, p(-1) = -16-8a e p'(-1) = 32+16a, todas corretas. Como s(-1) = 16 e s(2) = -35, as multiplicidades são 2 para -1 e 1 para 2. O enunciado do PDF (pág. 5 do caderno) bate com a transcrição. |

### Questão 5

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| abscissa de C | x_C = 5√3 − 9 (≈ −0,34) | x = 5√3 − 9 | igual | both | Mesmo valor. Refiz a conta: com x=1 na elipse 2x²+y²=6, y=±2, logo AB=4 e CA+CB=6. C está então na elipse de focos A e B, (x−1)²/5 + y²/9 = 1, que equivale a 9x²−18x+5y²=36. Fazendo 5·(2x²+y²=6) − (9x²−18x+5y²=36), sai x²+18x+6=0, com raízes x=−9±5√3. Como \|x\|≤√3, só fica 5√3−9≈−0,3397. Conferi em Python: y≈2,4019, CA≈1,3987, CB≈4,6013, perímetro = 10,000. O valor x²=156−90√3 citado pela resolução também está certo. Como x≠1, o triângulo não é degenerado. |

### Questão 6

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Questão 6 (número de sêxtuplas) | 235 sêxtuplas ordenadas | 235 sêxtuplas | igual | both | Conferi o enunciado no PDF original (pág. 6) e ele bate com a transcrição. A redução feita é válida: com S = x3+x4+x5, sai x2 = 6, x1 = 8 − 2x6 e S = 16 − x6. Como x1 ≥ 1, temos x6 ≤ 3, logo x6 ∈ {1,2,3}. Pelo método das estrelas e barras, o número de ternas positivas com soma S é C(S−1,2), o que dá C(14,2)+C(13,2)+C(12,2) = 91+78+66 = 235. O gabarito chega ao mesmo resultado com outra notação: P_14^{12,2} = 14!/(12!·2!) = 91, e assim por diante. Também testei todas as sêxtuplas por força bruta em Python, com cada xi ≥ 1, e o total foi 235. |

### Questão 7

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Questão 7 (valores inteiros de n) | n ∈ {−6, −4, 6, 8} (quocientes −10, −30, −10 e 18) | n ∈ {−6, −4, 6, 8} | igual | both | A transcrição confere com o enunciado original (p. 8 do PDF). A divisão está certa: (2n−1)(n²−2n−27) = 2n³−5n²−52n+27, então o resto é 90−27 = 63 e o quociente é E = 2n−1 + 63/(n²−2n−27). O denominador nunca se anula para n inteiro, porque (n−1)² = 28 não tem solução inteira. Como 28+d precisa ser quadrado perfeito, só sobram d = −3, que dá (n−1)² = 25 e n ∈ {−4, 6}, e d = 21, que dá (n−1)² = 49 e n ∈ {−6, 8}. Confirmei por força bruta em python, para \|n\| ≤ 100000, que estes são os únicos valores. Os quocientes saem −10, −30, −10 e 18, iguais aos da resolução. |

### Questão 8

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| a | 0 < x ≤ 1 ou 9 ≤ x < 10 | 0 < x ≤ 1 ou 9 ≤ x < 10 | igual | both | Os dois chegam à mesma condição, y(6−y) = x(10−x), com y = BF. A resolução usa coordenadas e produto escalar; o gabarito usa semelhança entre EBF e HAE. Para existir y em (0,6), é preciso x(10−x) ≤ 9, isto é, (x−1)(x−9) ≥ 0, que é o mesmo Δ ≥ 0 do gabarito. Restringindo a 0<x<10, sai o intervalo da resposta. A resolução ainda confere que y = 3 ± √((x−1)(x−9)) fica em (0,6), o que o gabarito não faz. Varri x de 0,001 a 9,999 e o resultado bateu com (0,1] ∪ [9,10). |
| b | Lados √10 e 3√10 (para x = 1 ou x = 9, com y = 3) | Lados 3√10 e √10 | igual | both | A área do retângulo inscrito é 60 − 6x − 10y + 2xy. Igualando a 30, obtém-se (x−5)(y−3) = 0. x = 5 é descartado pelo item a, então y = 3 e, daí, x(10−x) = 9, ou seja, x = 1 ou x = 9. Para x = 1, EF = √(81+9) = 3√10 e EH = √(1+9) = √10, com produto 30. Para x = 9 os valores apenas se invertem. Conferi numericamente: a área dá 30 e a relação (1) dá resíduo 0. |

### Questão 9

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| Área da seção | 5(2+√3) = 10+5√3 ≈ 18,66 (trapézio isósceles de bases 8 e 2, altura 2+√3) | 5(2+√3) | igual | both | Refiz a conta. A aresta lateral é ℓ² = 16/(2−√3) = 16(2+√3), a altura da pirâmide é h² = 16+16√3 e o apótema lateral é VM = 2(2+√3) = 2·tg75°. O plano paralelo à face VBC que passa por AD corta as arestas VE e VF nos pontos médios. Isso dá um trapézio de bases 8 e 2 com altura OT = VM/2 = 2+√3. Área = (8+2)/2·(2+√3) = 5(2+√3). Uma verificação numérica com vetores (interseção do plano com as arestas e área do polígono) deu 18,660254, que coincide com 5(2+√3). |

### Questão 10

| Item | Resolução | Gabarito | Veredito | Quem está certo | Comentário |
| --- | --- | --- | --- | --- | --- |
| único | k = 3 (no 1º quadrante f ∈ (√2−1, 2−√2]; no 3º quadrante f ∈ (√2+1, 2+√2]) | k = 3 | igual | both | Conferi o enunciado no PDF original (pág. 10) e ele coincide com a transcrição. Simplificando, f(x) = √2(\|cos x\|+\|sen x\|) − (sen x + cos x). No 1º quadrante, f = (√2−1)(sen x+cos x) = (2−√2)·sen(x+π/4) ∈ (√2−1, 2−√2] ≈ (0,414; 0,586], intervalo sem inteiros. No 3º quadrante, f = −(√2+1)(sen x+cos x) = −(2+√2)·sen(x+π/4) ∈ (√2+1, 2+√2] ≈ (2,414; 3,414], cujo único inteiro é 3. Conferi com uma amostragem numérica (200 mil pontos em cada quadrante): o 1º quadrante deu de 0,41421 a 0,58579 e o 3º de 2,41421 a 3,41421. Também testei o x dado na resolução, x = 3π/4 + arcsen(3(2−√2)/2) ≈ 3,429 rad. Ele está em (π, 3π/2) e dá f(x) = 3,000. A resolução e o gabarito chegam a k = 3 pelo mesmo caminho. |

## Pontos de dúvida

- **Q1** (solution): A resolução fecha com uma contagem condicional: '5 PAs crescentes, ou 10 contando as decrescentes'. Como (48,47,…,39) é uma PA diferente de (39,…,48), o enunciado ('todas as PAs') pede 10, que é o que o gabarito afirma. As 10 estão descritas, mas um corretor rigoroso pode preferir uma afirmação firme ('são 10 PAs') a deixar a contagem a cargo do leitor.
- **Q1** (key): A resolução do Poliedro tem problemas de notação. Faltam parênteses em 'S_10 = (a_1 + a_10 · 10)/2' e em '(2a_1 + 9r · 10)/2'. Além disso, a lista das decrescentes aparece concatenada, sem separadores ('…40,3957,54,…'), o que parece ser artefato de extração. Nada disso afeta o resultado.
- **Q1** (key): O gabarito não justifica por que a lista de razões para em r = 9. Falta a condição a₁ = (87−9r)/2 ≥ 1 ⇒ r ≤ 85/9; com r = 11 daria a₁ = −6. Também não justifica a redução das razões negativas à inversão das crescentes. A resolução conferida faz as duas justificativas de forma explícita.
- **Q2** (key): Na resolução do gabarito, o Caso 2 aparece como 'log_2(2^x+2) < −2x ⇒ 2^x + 2 > 2^(−2x)'. O sinal '<' está invertido: deveria ser '>'. Parece erro de digitação ou de extração do texto, porque a linha seguinte e a conclusão usam o sentido certo, e o resultado final não muda.
- **Q2** (solution): No Passo 1, a resolução justifica a passagem log2(2^x+2) > \|2x\| ⇒ 2^x + 2 > 2^\|2x\| dizendo 'Como \|2x\| ≥ 0 e log2 é crescente'. O motivo certo é que 2^(·) é crescente; o fato de \|2x\| ≥ 0 não tem papel aí. É só imprecisão de redação, sem efeito na conta.
- **Q4** (key): O gabarito tira a = -2 só de p(-1) = 0, sem usar p(2) = 0 nem a multiplicidade dupla de -1. A compatibilidade das condições só fica garantida depois, porque a divisão dá resto nulo. O argumento está completo, mas seria mais claro dizer que a divisão exata confirma a hipótese.
- **Q5** (key): A transcrição da resolução do gabarito tem erros de digitação que não afetam o resultado: "A = 1,2" e "centro 1,0" estão sem parênteses, e a fórmula aparece como "(x-1^2)/5" no lugar de (x−1)²/5. A forma expandida que o gabarito usa, 9x²−18x+5y²=36, está correta.
- **Q5** (solution): A resolução fixa A=(1,2) e B=(1,−2) sem perda de generalidade. Trocar os rótulos não muda a soma CA+CB nem a abscissa de C, então está tudo certo. Ela também observa que há dois pontos C possíveis, (x, ±y), com a mesma abscissa, e isso é coerente com o enunciado, que pede apenas a abscissa.
- **Q6** (key): O gabarito afirma que 1 ≤ x6 ≤ 3 sem justificar. O limite vem de x1 = 8 − 2x6 ≥ 1, junto com o fato de x6 ser inteiro. A resolução conferida faz essa justificativa. Isso afeta só a redação, não o resultado.
- **Q7** (key): Há erro de digitação no discriminante do gabarito. Para n² − 2n − (k+27) = 0, o certo é Δ = 4 + 4(k+27) = 4(k+28), mas o gabarito escreve 'Δ = 4 + 4k + 27' e 'm² = 4k + 28'. A conclusão (k+28 tem de ser quadrado perfeito) e a resposta final não mudam.
- **Q7** (solution): A resolução cita 'uma busca computacional em −2000 ≤ n ≤ 2000', o que não vale como argumento numa prova escrita. A demonstração algébrica já está completa sem isso: D(n) divide 63 e 28+D(n) tem de ser quadrado perfeito. Na versão entregue, convém tirar essa frase ou deixar claro que é só uma conferência.
- **Q8** (key): No item b, o gabarito escreve 'x−5y−3 = 0'. É erro de digitação de (x−5)(y−3) = 0: a sequência ('x = 5 é impossível, logo y = 3') confirma a fatoração correta. A resposta final não muda.
- **Q8** (statement): Os dois leem 'inscrito' como um vértice de EFGH em cada lado de ABCD, com G em CD e H em DA. É a leitura padrão e o enunciado não a declara. A resolução deixa essa hipótese explícita e mostra que G = (10−x, 6) cai no interior de CD.
- **Q9** (key): No texto da resolução do gabarito, a fórmula final saiu truncada: "(AD + PQOT)/2 = (8 + 2 · tg75°)/2 = 52 + √(3)". O certo seria (AD+PQ)·OT/2 = (8+2)·tg75°/2 = 5(2+√3). Parece só perda de formatação na transcrição, porque o valor final 5(2+√3) está correto.
- **Q9** (statement): O enunciado não diz a qual face lateral a seção é paralela. Só as duas faces cuja aresta da base é paralela à diagonal escolhida tornam a seção possível, e por simetria elas dão seções congruentes. A resolução justifica isso explicitamente; o gabarito assume sem comentar. Não muda a resposta.
- **Q10** (key): Na simplificação inicial, o gabarito escreve f(x) = √2 cos x + √2 sen x − sen x − cos x, sem os módulos (o certo é √(2cos²x) = √2\|cos x\|). Depois ele corrige isso ao tratar cada quadrante com o sinal certo, então o resultado não muda. Mesmo assim, como passagem isolada, a igualdade está errada.
- **Q10** (key): O gabarito mistura desigualdades estritas e não estritas no 1º quadrante: escreve √2/2 ≤ sen(x+π/4) ≤ 1, depois √2/2 < f/(2−√2) ≤ 1 e por fim √2−1 ≤ f ≤ 2−√2. Além disso, usa a mesma letra k para o período (2kπ) e para o inteiro procurado. São só questões de redação e não afetam a resposta.
- **Q10** (statement): O enunciado não diz se os pontos sobre os eixos (x = 0, π/2, π, 3π/2) contam como parte dos quadrantes. A resolução trata esse caso no passo 5: nesses pontos f vale √2−1 ou √2+1, que não são inteiros. Por isso a resposta k = 3 vale com qualquer das duas convenções.
