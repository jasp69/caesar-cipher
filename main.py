def caesar(start_text,shift_amount,cipher_direction):
  end_text_list=[]
  end_text_list+=start_text
  end_text=""

  if cipher_direction == "decode":
    shift_amount *= -1
    
  for i in range(0,len(end_text_list)):
    a=ord(end_text_list[i])
    a+=shift_amount
    b=chr(a)
    end_text+=b
  print(f"Here's the {cipher_direction}d result: {end_text}")




direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
