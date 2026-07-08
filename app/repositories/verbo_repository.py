from ..core.supabase import supabase

def get_verbo():
    
    definicao_verbo = supabase.table("verbo").select("*").execute()
    modos_verbais = supabase.table("modo_verbal").select("*").execute()
    tempos_verbais = supabase.table("tempo_verbal").select("*").execute()
    exemplos_verbais = supabase.table("exemplo_verbal").select("*").execute()


    exemplos = {}
    for linha in exemplos_verbais.data:
        tempo_id = linha["tempo_id"]
        frase = linha["frase"]
        exemplos.setdefault(tempo_id, []).append((frase))
    
    tempos_por_modo = {}
    for linha in tempos_verbais.data:
        modo_id = linha["modo_id"]
        id = linha["id"]
        nome = linha["nome"]
        tempos_por_modo.setdefault(modo_id, []).append(({
            "id": id,
            "nome": nome,
            "exemplos": exemplos.get(id, [])
        }))
    
    modos_formatados = []
    for linha in modos_verbais.data:
        id = linha["id"]
        nome = linha["nome"]
        verbo_id = linha["verbo_id"]
        modos_formatados.append({
            "id": id,
            "nome": nome,
            "tempos": tempos_por_modo.get(id, [])
        })

    resultado ={
        "id": definicao_verbo.data[0]["id"],
        "definicao": definicao_verbo.data[0]["definicao"],
        "modos": modos_formatados
    }


    return resultado