import java.util.List;

public class Data {
    private static Data info= new Data();
    private List<reunionI>Reuniones;

    public static Data getInstance() {
        if(info == null)
            info = new Data();
        return info;
    }
    //obtener list
    public List<reunionI> getReuniones() {
        return Reuniones;
    }
    public void setReuniones(List<reunionI> reunionIs) {
        this.Reuniones = reunionIs;
    }
 
}
