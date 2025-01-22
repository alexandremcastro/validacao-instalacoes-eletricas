import streamlit as st


def main():
    st.title("Validação do Prontuário de Instalações Elétricas (NR-10)")
    st.write("Verifique cada item e adicione observações, se necessário.")

    items = {
        "a": "Conjunto de procedimentos e instruções técnicas e administrativas de segurança e saúde, implantadas e relacionadas a esta NR e descrição das medidas de controle existentes.",
        "b": "Documentação das inspeções e medições do sistema de proteção contra descargas atmosféricas e aterramentos elétricos.",
        "c": "Especificação dos equipamentos de proteção coletiva e individual e o ferramental, aplicáveis conforme determina esta NR.",
        "d": "Documentação comprobatória da qualificação, habilitação, capacitação, autorização dos trabalhadores e dos treinamentos realizados.",
        "e": "Resultados dos testes de isolação elétrica realizados em equipamentos de proteção individual e coletiva.",
        "f": "Certificações dos equipamentos e materiais elétricos em áreas classificadas.",
        "g": "Relatório técnico das inspeções atualizadas com recomendações, cronogramas de adequações, contemplando as alíneas de 'a' a 'f'.",
    }

    # Formulário para validação
    with st.form(key="validation_form"):
        validations = {}
        observations = {}

        st.subheader("Itens para validação")
        for key, description in items.items():
            st.markdown(f"**{key.upper()}**: {description}")
            validations[key] = st.checkbox(
                f"Item {key.upper()} validado?", key=f"check_{key}"
            )
            observations[key] = st.text_area(
                f"Observação para o item {key.upper()} (opcional):", key=f"obs_{key}"
            )
            st.write("---")

        submit = st.form_submit_button("Enviar validação")

        if submit:
            st.success("Validação submetida com sucesso!")
            st.write("### Resumo das validações:")
            for key, validated in validations.items():
                status = "Validado" if validated else "Não validado"
                st.write(f"- **Item {key.upper()}**: {status}")
                if observations[key]:
                    st.write(f"  - Observação: {observations[key]}")


if __name__ == "__main__":
    main()
