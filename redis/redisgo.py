import redis


def cria_jogadores(red):
    
    #for n_jogador in range(50):
    #    red.delete("user:"+str(n_jogador))

    for n_jogador in range(50):
        num = str(n_jogador)
        red.hset("user:"+num, "name", "user"+num )
        red.hset("user:"+num, "cartela", "cartela"+num )
        red.hset("user:"+num, "score", "score"+num )

def cria_numeros(red):
    for n in range(99):
        red.sadd("numeros",n+1)

def cria_cartelas(red):
    for user in range(50):
        red.delete("cartela"+str(user))

    for user in range(50):
        cria_numeros(red)
        for i in range(15):
            n = red.srandmember('numeros')
            red.sadd("cartela"+str(user),n)
            red.srem("numeros",n)

def sorteia(red):
    cria_numeros(red)
    bingo = 0

    for n in range(50):
        red.set("score"+str(n),0)

    while bingo == 0 :
        numero = red.srandmember('numeros')
        red.srem('numeros', numero)

        for n in range(50):
            cartela = "cartela"+str(n)
            score = "score"+str(n)
            if red.sismember(cartela,numero):
                red.incr(score,1)
            if int(red.get(score)) == 15: 
                bingo += 1
                print(score)
            
        

def main():
    print(20*'-')
    print('------REDISGO-------')
    print(20*'-')

    red = redis.Redis(host='localhost', port=6379, db=0)


    cria_jogadores(red)
    cria_cartelas(red)
    sorteia(red)
 


if __name__ == '__main__':
    main()