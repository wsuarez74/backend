from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from sqlalchemy.orm import Session
from database import SessionLocal
from queries import obtener_cliente_por_nombre, obtener_total_compras_cliente, obtener_deuda_cliente, obtener_credito_disponible, analizar_si_puede_comprar

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/total_compras/{nombre}")
def total_compras(nombre: str, db: Session = Depends(get_db)):
    cliente = obtener_cliente_por_nombre(db, nombre)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    total = obtener_total_compras_cliente(db, cliente.id)
    return {"cliente": cliente.nombre, "total_compras": total}

@app.get("/deuda/{nombre}")
def deuda_cliente(nombre: str, db: Session = Depends(get_db)):
    cliente = obtener_cliente_por_nombre(db, nombre)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    deuda = obtener_deuda_cliente(db, cliente.id)
    return {"cliente": cliente.nombre, "deuda": deuda}

@app.get("/credito/{nombre}")
def credito_cliente(nombre: str, db: Session = Depends(get_db)):
    cliente = obtener_cliente_por_nombre(db, nombre)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    credito = obtener_credito_disponible(db, cliente.id)
    return {"cliente": cliente.nombre, "credito_disponible": credito}

@app.get("/evaluar/{nombre}")
def evaluar_cliente(nombre: str, db: Session = Depends(get_db)):
    cliente = obtener_cliente_por_nombre(db, nombre)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    evaluacion = analizar_si_puede_comprar(db, cliente.id)
    return {"cliente": cliente.nombre, "evaluacion": evaluacion}

# Ejecutar el servidor con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
