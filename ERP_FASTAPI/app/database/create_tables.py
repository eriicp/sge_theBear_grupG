import psycopg2

def create_table():
    conn = psycopg2.connect(
        database = "the_bear",
        password = "admin",
        user = "admin",
        host = "localhost",
        port = "5432"
    )

    cursor = conn.cursor()
    
    sql_empleats = '''
    CREATE TABLE Empleats (
        Id_Empleat SERIAL,
        Nombre_Empleat VARCHAR(100),
        Puesto_Empleat VARCHAR(100),
        Departament_Empleat VARCHAR(100),
        Email_Empleat  VARCHAR(100),
        Telefon_Empleat VARCHAR(100),
        Id_Gerent_Empleat INT,
        CONSTRAINT PK_ID_EMPLEAT PRIMARY KEY (Id_Empleat),
        CONSTRAINT FK_ID_GERENT FOREIGN KEY (Id_Gerent_Empleat)
            REFERENCES Empleats (Id_Empleat)
    );
    '''

    sql_planificacio = '''
    CREATE TABLE Planificacio (
        Id_Planificacio SERIAL,
        Projecte VARCHAR(100),
        Tasca VARCHAR(100),
        Responsable INT,
        Data_Inici DATE,
        Data_Fi DATE,
        Estat_Tasca VARCHAR(50),
        Material_Utilitzat TEXT,
        Comentaris TEXT,
        CONSTRAINT PK_ID_PLANIFICACIO PRIMARY KEY (Id_Planificacio),
        CONSTRAINT FK_RESPONSABLE FOREIGN KEY (Responsable)
            REFERENCES Empleats(Id_Empleat)
    );
    '''

    sql_events = '''
    CREATE TABLE Events (
        Id_Event SERIAL,
        Nom_Event VARCHAR(100),
        Data_Event DATE,
        Hora_Event TIME,
        Ubicacio_Event VARCHAR(200),
        Organitzador_Event INT,
        Estat_Event VARCHAR(50),
        Entrades_Disponibles INT,
        Privat BOOLEAN,
        CONSTRAINT PK_ID_EVENT PRIMARY KEY (Id_Event),
        CONSTRAINT FK_ORGANITZADOR_EVENT FOREIGN KEY (Organitzador_Event)
            REFERENCES Empleats(Id_Empleat)
    );
    '''

    sql_costos = '''
    CREATE TABLE Costos (
        Id_Cost SERIAL,
        Descripcio VARCHAR(150),
        Categoria VARCHAR(100),
        Quantitat DECIMAL(10,2),
        Data_Cost DATE,
        Pagat_Per INT,
        CONSTRAINT PK_ID_COST PRIMARY KEY (Id_Cost),
        CONSTRAINT FK_PAGAT_PER FOREIGN KEY (Pagat_Per)
            REFERENCES Empleats(Id_Empleat)
    );
    '''

    sql_compres = '''
    CREATE TABLE Compres (
        Id_Compra SERIAL,
        Data_Compra DATE,
        Proveidor VARCHAR(100),
        Producte_Compra VARCHAR(100),
        Quantitat INT,
        Preu_Unitari DECIMAL(10,2),
        Total DECIMAL(10,2),
        Estat_Comanda VARCHAR(50),
        CONSTRAINT PK_ID_COMPRA PRIMARY KEY (Id_Compra)
    );
    '''

    sql_punts_de_venda = '''
    CREATE TABLE Punts_de_Venda (
        Id_Punt SERIAL,
        Nom_Punt VARCHAR(100),
        Producte VARCHAR(100),
        Quantitat INT,
        Preu_Total DECIMAL(10,2),
        Metode_Pagament VARCHAR(50),
        Tiquet_Email BOOLEAN,
        Data_Venda DATE,
        CONSTRAINT PK_ID_PUNT PRIMARY KEY (Id_Punt)
    );
    '''

    sql_compres_punts = '''
    CREATE TABLE Compres_Punts (
        Id_Compra INT,
        Id_Punt INT,
        CONSTRAINT FK_COMPRA FOREIGN KEY (Id_Compra)
            REFERENCES Compres(Id_Compra),
        CONSTRAINT FK_PUNT FOREIGN KEY (Id_Punt)
            REFERENCES Punts_de_Venda(Id_Punt),
        PRIMARY KEY (Id_Compra, Id_Punt)
    );
    '''

    sql_vendes = '''
    CREATE TABLE Vendes (
        Id_Venda SERIAL,
        Data_Venda DATE,
        Client_Venda VARCHAR(100),
        Producte_Venda VARCHAR(100),
        Quantitat INT,
        Preu_Unitari DECIMAL(10,2),
        Total DECIMAL(10,2),
        Metode_Pagament VARCHAR(50),
        Id_Punt INT,
        CONSTRAINT PK_ID_VENDA PRIMARY KEY (Id_Venda),
        CONSTRAINT FK_PUNT_VENDA FOREIGN KEY (Id_Punt)
            REFERENCES Punts_de_Venda(Id_Punt)
    );
    '''

    sql_calendari = '''
    CREATE TABLE Calendari (
        Id_Reunio SERIAL,
        Nom_Reunio VARCHAR(100),
        Data_Reunio DATE,
        Hora_Inici TIME,
        Hora_Fi TIME,
        Ubicacio_Reunio VARCHAR(150),
        Etiquetes TEXT,
        Recurrencia BOOLEAN,
        CONSTRAINT PK_ID_REUNIO PRIMARY KEY (Id_Reunio)
    );
    '''

    sql_calendari_empleats = '''
    CREATE TABLE Calendari_Empleats (
        Id_Reunio INT,
        Id_Empleat INT,
        CONSTRAINT FK_REUNIO FOREIGN KEY (Id_Reunio)
            REFERENCES Calendari(Id_Reunio),
        CONSTRAINT FK_EMPLEAT_CALENDARI FOREIGN KEY (Id_Empleat)
            REFERENCES Empleats(Id_Empleat),
        PRIMARY KEY (Id_Reunio, Id_Empleat)
    );
    '''

    sql_planificacio_compres = '''
    CREATE TABLE Planificacio_Compres (
        Id_Planificacio INT,
        Id_Compra INT,
        CONSTRAINT FK_PLANIF FOREIGN KEY (Id_Planificacio)
            REFERENCES Planificacio(Id_Planificacio),
        CONSTRAINT FK_COMPRA_PLANIF FOREIGN KEY (Id_Compra)
            REFERENCES Compres(Id_Compra),
        PRIMARY KEY (Id_Planificacio, Id_Compra)
    );
    '''

    cursor.execute(sql_empleats)
    cursor.execute(sql_planificacio)
    cursor.execute(sql_events)
    cursor.execute(sql_costos)   
    cursor.execute(sql_punts_de_venda) 
    cursor.execute(sql_compres)
    cursor.execute(sql_vendes)
    cursor.execute(sql_calendari)
    cursor.execute(sql_compres_punts)
    cursor.execute(sql_calendari_empleats)
    cursor.execute(sql_planificacio_compres)


    conn.commit()
    conn.close()
    cursor.close()

    return {"TAULES FETES AMB EXIT!"}
create_table()