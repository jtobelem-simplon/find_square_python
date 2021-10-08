'''
Précalcule une matrice prefixe pour pouvoir calculer is_free en O(1)
'''
def compute_prefix(carte, vide, plein):
    prefix = [[0]*len(carte[0])]*len(carte)

    for i in range(len(carte)):
        for j in range(len(carte[0])):
            m_ij = 1 if carte[i][j] in [vide,plein] else 0

            prefix[i][j] = m_ij 
            
            if j>0 :
                prefix[i][j] += prefix[i][j-1]
            
            if i>0 :
                prefix[i][j] += prefix[i-1][j]-prefix[i-1][j-1]

            if i>0 and j>0 :
                prefix[i][j] -= prefix[i-1][j-1]
    
    print(prefix)
    return prefix

def is_free(prefix, pos_line, pos_col, size) :
    area = size*size
    s = prefix[pos_line+size][pos_col+size] - prefix[0][pos_col] - prefix[pos_line][0] + prefix[pos_line][pos_col]
    #print(s, area)
    return s == area