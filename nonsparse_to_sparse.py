import io

# INPUT : non - sparse data in nonsparse.txt
# OUTPUT: sparse format in sparse.txt
parsed_normals=open('sparse.txt','w')

for line in file('nonsparse.txt'):
	tokens=line.split()
	target=float(tokens[0])
	#target=float(tokens[1])
	tokens=[tuple(t.split(':')) for t in tokens[1:]]
	#priint output[0]
	normals=[]
        for i in range(0,len(tokens)-1):
		m= tokens[i]
		normals.append(float(m[1]))
	#parsed_normals.write("".join(normals))
	for item in normals:
            parsed_normals.write("%f " % item)
        print>>parsed_normals , '\n'
	del normals[:]







'''
KEYWORDS = ['test', '<strong class="highlight">text</strong>']
counterline = []
counter = 0

print logfile[11]
'''
