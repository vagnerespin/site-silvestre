
# 📌 Cadastro de Espécies - Exemplo completo com imagem real
@app.route('/add_especie', methods=['GET', 'POST'])
@login_required
def add_especie():
    locais = Local.query.all()
    if request.method == 'POST':
        nome_comum = request.form['nome_comum']
        nome_cientifico = request.form['nome_cientifico']
        descricao = request.form['descricao']
        local_id = request.form['local_id']
        imagem = request.files['imagem']

        # Validação do caminho da imagem
        imagem_url = None
        if imagem and imagem.filename != "":
            caminho = os.path.join('static', 'img', imagem.filename)
            imagem.save(caminho)
            imagem_url = f'img/{imagem.filename}'  # Caminho relativo para uso no HTML

        nova_especie = Especie(
            nome_comum=nome_comum,
            nome_cientifico=nome_cientifico,
            descricao=descricao,
            local_id=local_id,
            imagem_url=imagem_url
        )
        db.session.add(nova_especie)
        db.session.commit()
        return redirect(url_for('main.listar_especies'))

    return render_template('add_especie.html', locais=locais)
