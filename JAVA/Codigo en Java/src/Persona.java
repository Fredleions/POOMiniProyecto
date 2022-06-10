public class Persona {

    private String nombre;
    private String profesion;
    private String sexo;
    private int edad;

    public Persona(){
        this.setEdad(0);
    }


    public Persona(String nombre, String profesion, String sexo, int edad) {
        this.nombre = nombre;
        this.profesion = profesion;
        this.sexo = sexo;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getProfesion() {
        return profesion;
    }

    public void setProfesion(String profesion) {
        this.profesion = profesion;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }


    public void validarValor(double edad) {
        if (edad < 0) {
            throw new IllegalArgumentException("La edad No puede ser negativa");
        }
    }

}
