from sqlalchemy.orm import Session
from models import Cliente, Venta, Cobranza

def obtener_cliente_por_nombre(db: Session, nombre: str):
    return db.query(Cliente).filter(Cliente.nombre.ilike(f"%{nombre}%")).first()

def obtener_total_compras_cliente(db: Session, cliente_id: int):
    total = db.query(Venta).filter(Venta.cliente_id == cliente_id).with_entities(Venta.monto).all()
    return sum([t[0] for t in total])

def obtener_deuda_cliente(db: Session, cliente_id: int):
    cobranza = db.query(Cobranza).filter(Cobranza.cliente_id == cliente_id).first()
    return cobranza.deuda if cobranza else 0

def obtener_credito_disponible(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    return cliente.credito_disponible if cliente else 0

def analizar_si_puede_comprar(db: Session, cliente_id: int):
    deuda = obtener_deuda_cliente(db, cliente_id)
    credito = obtener_credito_disponible(db, cliente_id)

    if deuda > credito:
        return "El cliente NO puede comprar, su deuda supera su crédito disponible."
    elif deuda > 0:
        return "El cliente puede comprar, pero tiene deudas pendientes."
    else:
        return "El cliente puede comprar sin restricciones."

