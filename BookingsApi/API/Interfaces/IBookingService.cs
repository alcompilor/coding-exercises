using BookingsApi.Models;

namespace BookingsApi.Interfaces
{
    public interface IBookingService
    {
        IEnumerable<Booking> GetAll();
        Booking? GetById(int id);
        Booking Create(Booking booking);
        bool Cancel(int id);
        bool HasOverlap(int id, DateTime from, DateTime to);
    }
}
