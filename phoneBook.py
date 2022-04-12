# Kullanicilari eklemek, cikarmak ya da guncellemek icin bir dict olusturuldu.
phoneBook = {}
# Her islemin sonunda tekrar degiskene girebilmesi icin daima true yapildi.
while True:
    # Degiskene deger tanimlanmistir. 5 islemimiz vardir ve integer olarak tanimlanmistir.
    # Kullanici ekleme, silme, guncelleme, listeleme degerleri verilmistir.
    transaction = int(input("""
    1 - Add user
    2 - Delete user
    3 - Update user
    4 - List of the Phone Book
    5 - Exit
    6 - Delete All users
    Select your transaction : """))
    # Girilen degere gore if blogumuzun calismasi gerceklestirildi.
    # Eger deger 1 ise,
    if(transaction == 1):
        # Name degiskenine deger girilir.
        name = str(input("Enter an username:"))
        # PhoneNumber degiskenine integer value girilir.
        phoneNumber = int(input("Enter a phone number:"))
        # phoneBook dict'ine key'i name, value'su phoneNumber olan bir pair atanir.
        phoneBook[name] = phoneNumber
        # Basariyla eklendi.
        print("Successfully added")
    # Eger deger 2 ise,
    elif(transaction == 2):
        # Name degiskenine string value girilir.
        name = str(input("Enter an username:"))
        # phoneBook dict'te key'i name olan deger silinir.
        phoneBook.pop(name)
        # Basariyla silindi.
        print("Successfully deleted")
    # Eger deger 3 ise,
    elif(transaction == 3):
        # Degiskene deger tanimlanmistir. 2 islemimiz vardir ve integer olarak tanimlanmistir.
        # Kullanici adi ya da numarisi degistirilebilir.
        transaction = int(input("""
        1 - Update User Name
        2 - Update Phone Number
        Select your transaction : """))
        # Eger deger 1 ise,
        if(transaction == 1):
            # Name degiskenine deger girilir.
            name = str(input("Enter an username:"))
            # Name key'ine ait value tutulur.
            value = phoneBook[name]
            # newName adinda bir degiskene yeni kullanici ismi girilir.
            newName = str(input("Enter a new username:"))
            # phoneBook dict'te key'i name olan deger silinir.
            phoneBook.pop(name)
            # Name degiskenine deger girilir.
            phoneBook[newName] = value
            # Basariyla guncellendi.
            print("Successfully updated")
        # Eger deger 2 ise,
        elif(transaction == 2):
            # Name degiskenine deger girilir.
            name = str(input("Enter an username:"))
            # PhoneNumber degiskenine integer value girilir.
            phoneNumber = int(input("Enter a phone number:"))
            # Key'i name olan pair'in phonenumber'e guncellendi.
            phoneBook[name] = phoneNumber
            # Basariyla guncellendi.
            print("Successfully updated")
    elif(transaction == 4):
        # PhoneBook ciktisi alinir.
        print("PhoneBook")
        # Sayacimiz 1 den baslar.
        count = 1
        # For kullanilarak phoneBook dict'te her key dolasilarak ciktisi alinir.
        for k in phoneBook:
            # Ilk suslu parantez icine count, ikinci suslu parantez icine key, ucuncu parantez icinede phoneBook'ta key'e ait value yazilir.
            print("{}. User Name : {} | Phone Number : {}".format(count,k,phoneBook[k]))
            # Count'umuz da 1 artar.
            count +=1
        # Listelendi ciktisi alinir
        print("Listed")
    # Eger deger 5 ise,
    elif(transaction == 5):
        # Donguden cikilir
        break
    # Degerlerden herhangi biri girilmediginde

    elif(transaction == 6):
        phoneBook.clear()
    else:
        # Hatali giris ciktisi alinir.
        print("Wrong Input!/n")










