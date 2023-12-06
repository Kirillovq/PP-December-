INSERT INTO client(id_client,name,surname,number_telephone,address,email) VALUES (1,'Андрей','Соломонов','+79047525168','г.Волгоград,ул.Ленина д.21','andrey1313@gmail.com');
INSERT INTO client(id_client,name,surname,number_telephone,address,email) VALUES (2,'Сергей','Филипов','+79608432323','г.Волгоград,ул.Тулака д.51','sergey144@gmail.com');
INSERT INTO client(id_client,name,surname,number_telephone,address,email) VALUES (3,'Максим','Фролов','+79173853028','г.Волгоград,ул.Елецкая д.42','maksim228@gmail.com');
INSERT INTO client(id_client,name,surname,number_telephone,address,email) VALUES (4,'Дмитрий','Миронов','+79173123022','г.Волгоград,ул.Елецкая д.22','dima228@gmail.com');
INSERT INTO client(id_client,name,surname,number_telephone,address,email) VALUES (5,'Данил','Смирнов','+79533851328','г.Волгоград,ул.Тулака д.132','danich228@gmail.com');

INSERT INTO executor(id_executor, name, surname, number_telephone, object_management) VALUES (1,'Давид','Ефимцов','+79047515156','Объекты под управлением: 1 ');
INSERT INTO executor(id_executor, name, surname, number_telephone, object_management) VALUES (2, 'Олег','Дмитриенко', '+79047151548', 'Объекты под управлением: 3');
INSERT INTO executor(id_executor, name, surname, number_telephone, object_management) VALUES (3, 'Вадим', 'Давыдов','+79603411212', 'Объекты под управлением: 4');
INSERT INTO executor(id_executor, name, surname, number_telephone, object_management) VALUES (4, 'Вадим', 'Олегов','+79610742223', 'Объекты под управлением: 2');
INSERT INTO executor(id_executor, name, surname, number_telephone, object_management) VALUES (5, 'Дамир', 'Давыдов','+79433454212', 'Объекты под управлением: 5');

INSERT INTO ordeer(ID_ORDER, DATE_CREATE, OBJECT, TYPE_REPAIR, DESCRIPTION_OBJECT, CLIENT, DATE_END, EXECUTOR) VALUES (1,'10.10.2023','Частный дом','Косметический','-',2,'',)