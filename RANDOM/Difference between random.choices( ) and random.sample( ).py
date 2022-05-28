# Difference between random.choices( ) and random.sample( )?
import random
language=['English','Chinese','Hindi','Arabic','Bengali','Portuguese','Russian','Turkish' ]
choices=random.choices(language,k=10)
print(choices)
sample= random.sample(language,k=5)
print(sample)
