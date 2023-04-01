import hashlib
def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(Self,data,hash,prev_hash):
        Self.data = data
        Self.hash = hash
        Self.prev_hash = prev_hash

class Blockchain:
    def __init__(Self):
        hashLast = hashGenerator("GEN_LAST")
        hashStart = hashGenerator("GEN_HASH")

        genesis = Block('MR' , hashStart , hashLast)
        Self.chain = [genesis]

    def Add_block(Self,data):
        prev_hash = Self.chain[-1].hash
        hash = hashGenerator(prev_hash)
        block = Block(data,hash,prev_hash)
        Self.chain.append(block)

bc = Blockchain()
bc.Add_block('1')
bc.Add_block('2')
bc.Add_block('3')
bc.Add_block('4')
bc.Add_block('5')
bc.Add_block('6')


for block in bc.chain:
    print(block.__dict__)


    
        
        
