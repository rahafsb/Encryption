# DAES Encryption

Encryption:
State=M
State = SubBytes(State)
State = AddRoundKey(State, K)=(L,R)
C = (R, L xor R xor K[0..7])
Decryption:
State = C = (R, L xor R xor K[0..7])
State = (L xor R xor K[0..7] xor R xor K[0..7], R) = (L, R)
State = AddRoundKey(State, K)
State = InvSubBytes(State)
M = State

Double DEAS Encryption:
C = Encryption(Encryption(M, K1), K2)

Double DAES Decryption:
M = Decryption(Decryption(C, K2), K1)


python daes.py -e <message path> <key path> <output path>
  message path - location of the file where the message you want to encrypt is located.
  key path - the file location of the encryption keys, the keys are chained one after the other.
  output path - the location of the file to which you must write the encryption output.

python daes.py -d <cipher path> <key path> <output path>
  cipher path - the location of the file where the encrypted message is located
  key path - the location of the file where the encryption keys are located, the keys are chained one after the other.
  output path - the location of the file to which you must write the decoding output

python daes.py -b <message1 path> <cipher1 path> <message2 path> <cipher2 path> <key path>
  message path - the location of the file where the text of the original messages is written
  cipher path - the location of the file where the encryption result of the messages is written
  key path - the location of the file where you must write what you discovered about the encryption keys. 
  The decoded bits of the encryption keys are concatenated together.
