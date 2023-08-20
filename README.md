# DAES Encryption

Encryption:<br>
State=M <br>
State = SubBytes(State) <br>
State = AddRoundKey(State, K)=(L,R) <br>
C = (R, L xor R xor K[0..7]) <br> <br> <br>
Decryption:<br>
State = C = (R, L xor R xor K[0..7]) <br>
State = (L xor R xor K[0..7] xor R xor K[0..7], R) = (L, R) <br>
State = AddRoundKey(State, K) <br>
State = InvSubBytes(State) <br>
M = State <br><br><br>

Double DEAS Encryption: <br>
C = Encryption(Encryption(M, K1), K2) <br><br><br>

Double DAES Decryption:<br>
M = Decryption(Decryption(C, K2), K1)<br><br><br>


python daes.py -e <message path> <key path> <output path><br>
  message path - location of the file where the message you want to encrypt is located.<br>
  key path - the file location of the encryption keys, the keys are chained one after the other.<br>
  output path - the location of the file to which you must write the encryption output.<br><br><br>

python daes.py -d <cipher path> <key path> <output path><br>
  cipher path - the location of the file where the encrypted message is located<br>
  key path - the location of the file where the encryption keys are located, the keys are chained one after the other.<br>
  output path - the location of the file to which you must write the decoding output<br><br><br>

python daes.py -b <message1 path> <cipher1 path> <message2 path> <cipher2 path> <key path> <br>
  message path - the location of the file where the text of the original messages is written <br>
  cipher path - the location of the file where the encryption result of the messages is written<br>
  key path - the location of the file where you must write what you discovered about the encryption keys. 
  The decoded bits of the encryption keys are concatenated together.
