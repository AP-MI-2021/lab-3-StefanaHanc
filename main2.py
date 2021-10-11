def afisare_meniu ():
    print("MENIU")
    print("1.Citeste datele ")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea ca suma numerelor este număr prim ")
    print("3.Determinare cea mai lungă subsecvență cu proprietatea ca numărul de cifre este în ordine descrescătoare.")
    print("4.Determinare cea mai lungă subsecvență cu proprietatea ca numărerele sa fie palindrome.")
    print("5.Iesie ")


def citire_date_problema():
    l=[]
    n=int(input("Dati numarul de elemente "))
    l=input("Dati lista cu elemente cu virgula ")
    l=[int(x) for x in l.split(",")]
    return l


def is_prim(x):
    '''
    Verifica daca numarul primit este prim
    :param x: Numarul verificat
    :return: True in caz ca numarul este prim ,false in caz contrar
    '''
    if x<2:
        return False
    for i in range(2,x//2 + 1):
        if x%i==0:
            return False
    return True

def test_is_prim():
    assert  is_prim(3) is True
    assert is_prim(2) is True
    assert is_prim(24) is False


def suma_numere(l):
    '''
    Calculam suma unor numere
    :param l: Lista de nr intregi
    :return: Suma numerelor din lista
    '''
    s=0
    for x in range(len(l)):
        s=s+l[x]
    return s


def get_longest_sum_is_prime(l):
    """
    Determinare cea mai lungă subsecvență cu proprietatea ca suma numerelor este număr prim
    :param l:Lista care este citita
    :return: Secventa maxima cu propirtatea ca suma numerelor este numar prim
    """
    secventaMax=[]
    for i in range (len(l)):
        for j in range (i,len(l)):
            suma=suma_numere(l[i:j+1])
            if is_prim(suma)==True and len(l[i:j+1])>len(secventaMax):
                secventaMax=l[i:j+1]
    return secventaMax


def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([1,2,3,4,5])==[1,2]
    assert get_longest_sum_is_prime([1,2,3,5])==[1,2,3,5]
    assert get_longest_sum_is_prime([1,2])==[1,2]
test_get_longest_sum_is_prime()


def numerele_sunt_descrescatoare(l):
    """
    Determina daca o lista este ordonata descrescator
    :param l: lista care este verifiata
    :return: True in cazul ca lista este ordonata desresctor si false in caz contrar
    """
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            return False
    return True
def test_numerele_sunt_descrescatoare():
    assert numerele_sunt_descrescatoare([1,2,3]) is False
    assert numerele_sunt_descrescatoare([3,2,4]) is False
    assert numerele_sunt_descrescatoare([5,4,3,2,0]) is True


def get_longest_digit_count_desc(l):
    """
    Determina cea mai lunga secventa cu propietatea sa fie ordonata descrescator
    :param l:Lista care trebuie verificata
    :return: Lista maxima determinata
    """
    lungMaxDesc=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if numerele_sunt_descrescatoare(l[i:j+1]) and len(lungMaxDesc)<len(l[i:j+1]):
                lungMaxDesc=l[i:j+1]
    return lungMaxDesc

def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([1,2,3,4,5])==[1]
    assert get_longest_digit_count_desc([5,4,6,2,1])==[6,2,1]
    assert get_longest_digit_count_desc([543,4,3,123])==[543,4,3]


def is_palindrom(x):
    """
    Verificam daca un numar este palindrom
    :param x: Numarul pe care il verificam
    :return: True in caz ca e palinfrom false in caz contrar
    """
    copie=x
    y=0
    while copie!=0:
        y=copie%10+y*10
        copie=copie//10
    if y==x:
        return True
    return False

def are_all_palindrom(l):
    """
    Verifica daca toate numerele dintr-o lista sunt palindroame
    :param lst:
    :return:True daca toate numerele din lista sunt palindroame, False in caz contrar
    """
    for x in l:
        if not is_palindrom(x):
            return False
    return True


def test_are_all_palindromes():
    assert are_all_palindrom([121,232]) is True

def test_is_palindrom():
    assert is_palindrom(123) is False
    assert is_palindrom(121) is True

test_is_palindrom()


def get_longest_all_palindromes(l):
    """
    Returnam ea mai lunga secventa cu propietatea ca numerele sunt palindroame
    :param l: Lista verificata
    :return: Cea mai lunga seccventa
    """
    lungMaxDesc = []
    for i in range(len(l)):
        for j in range(len(l)):
            if are_all_palindrom(l[i:j+1]) and len(lungMaxDesc)<len(l[i:j+1]):
                lungMaxDesc=l[i:j+1]
    return lungMaxDesc

def test_get_longest_all_programes():
    assert get_longest_all_palindromes([121,123321,12])==[121,123321]
    assert get_longest_all_palindromes([12,21])==[]
    assert get_longest_all_palindromes([121,312,23])==[121]

def main():
    test_get_longest_all_programes()
    test_numerele_sunt_descrescatoare()
    test_get_longest_digit_count_desc()
    l = []
    while True:
        afisare_meniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l =citire_date_problema()
        elif optiune == "2":
            print(get_longest_sum_is_prime(l))
        elif optiune == "3":
            print(get_longest_digit_count_desc(l))
        elif optiune=="4":
            print(get_longest_all_palindromes(l))
        elif optiune=="5":
            break
        else:
            print("Optiune gresita! Reincercati!")
if __name__=="__main__":
    main()