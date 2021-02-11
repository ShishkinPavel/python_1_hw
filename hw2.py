import random


# I apologize for the comments in Czech, but I'm too lazy to rewrite them

# Adding a random number to the playing field

def add_random(row, candidates):
    # Kontrola volného místa
    if 0 in row:
        # Vytvářím seznam pro umístění indexů nuly ze seznamu row
        indexes_0 = [i for i in range(len(row)) if row[i] == 0]
        # Dávám náhodné číslo na náhodné prázdné místo
        row[random.choice(indexes_0)] = random.choice(candidates)
        return True
    else:
        return False


# Shift left or right

def slide_basic(row, to_left):
    # Dělám kopii seznamu pro další kontrolu
    check_row = row.copy()
    # Poznávám délku seznamu
    len_row = len(row)
    # Kontroluji velikost seznamu
    if len_row <= 0:
        return False
    # Pokud se posune doprava, otočím list, udělám všechny
    # akce, jako by se posunul doleva, pak otočím seznam zpět
    if to_left is False:
        row.reverse()
    # Odstraním všechny nuly ze seznamu
    while 0 in row:
        row.remove(0)
    # Přidávám nuly na konec seznamu,
    # dokud velikost seznamu nebude jako dříve
    while len(row) != len_row:
        row.append(0)
    # Budoucí index
    index = 0
    while len_row > 1:
        if row[index] == row[index + 1] and row[index + 1] != 0:
            # Vynásobím číslo pozicí i o 2
            row[index] *= 2
            # Odstraníme následující číslo
            del row[index + 1]
            # Přidávám na konec seznamu 0
            row.append(0)
        index += 1
        len_row -= 1
    # Otočím seznam zpět, pokud je to nutné
    if to_left is False:
        row.reverse()
    # Pokud se seznam změnil
    if check_row != row:
        return True
    else:
        return False


# Shift with multiple merging

def slide_multi(row, to_left):
    # Na začátku stále totéž
    check = row.copy()
    len_row = len(row)
    if len_row <= 0:
        return False
    if to_left is False:
        row.reverse()
    while 0 in row:
        row.remove(0)
    while len(row) != len(check):
        row.append(0)
    index = 0
    while len_row > 1:
        # počet opakování čísla
        count_duplicate = 1
        # je třeba uložit index i
        check_index = index
        while len_row > 1 and row[index] == \
                row[index + 1] and row[index + 1] != 0:
            # Zvyšuji počet opakování
            count_duplicate += 1
            # Nahrazuji nulami zbývající opakující se čísla
            del row[check_index + 1]
            row.append(0)
            len_row -= 1
        # Vynásobím původní číslo počtem opakování
        row[check_index] *= count_duplicate
        # Vracíme i do původní hodnoty
        index = check_index
        index += 1
        len_row -= 1
    if to_left is False:
        row.reverse()
    if check != row:
        return True
    else:
        return False


def main():
    # --- add_random ---

    results = [[2, 1, 2, 0, 4], [2, 3, 2, 0, 4],
               [2, 0, 2, 1, 4], [2, 0, 2, 3, 4]]

    count = [0 for x in results]

    for i in range(1000):
        row = [2, 0, 2, 0, 4]
        assert add_random(row, [1, 3])
        for j in range(len(results)):
            if row == results[j]:
                count[j] += 1
                break

    assert sum(count) == 1000
    for freq in count:
        # if add_random is correct, the probability that this assert fails
        # is less than 1 in 500 000 000 (six sigma)
        assert 167 < freq < 333

    assert not add_random([2, 1, 2, 3, 4], [7, 5])

    # --- slide_basic ---

    row = [0, 2, 2, 0]
    assert slide_basic(row, True)
    assert row == [4, 0, 0, 0]
    row = [2, 2, 2, 2, 2]
    assert slide_basic(row, False)
    assert row == [0, 0, 2, 4, 4]
    row = [2, 0, 0, 2, 4, 2, 2, 2]
    assert slide_basic(row, True)
    assert row == [4, 4, 4, 2, 0, 0, 0, 0]
    row = [3, 0, 6, 3, 3, 3, 6, 0, 6]
    assert slide_basic(row, False)
    assert row == [0, 0, 0, 0, 3, 6, 3, 6, 12]
    row = [16, 8, 4, 2, 0, 0, 0]
    assert not slide_basic(row, True)
    assert row == [16, 8, 4, 2, 0, 0, 0]

    # --- slide_multi ---

    row = [0, 2, 2, 0]
    assert slide_multi(row, True)
    assert row == [4, 0, 0, 0]
    row = [2, 2, 2, 2, 2]
    assert slide_multi(row, False)
    assert row == [0, 0, 0, 0, 10]
    row = [2, 0, 0, 2, 4, 2, 2, 2]
    assert slide_multi(row, True)
    assert row == [4, 4, 6, 0, 0, 0, 0, 0]
    row = [3, 0, 6, 3, 3, 3, 6, 0, 6]
    assert slide_multi(row, False)
    assert row == [0, 0, 0, 0, 0, 3, 6, 9, 12]
    row = [16, 8, 4, 2, 0, 0, 0]
    assert not slide_multi(row, True)
    assert row == [16, 8, 4, 2, 0, 0, 0]


if __name__ == '__main__':
    main()
